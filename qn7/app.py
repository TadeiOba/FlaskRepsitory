from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index_crud.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        item_name = request.form['item_name']
        new_item = Item(name=item_name)
        db.session.add(new_item)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:item_id>', methods=['GET', 'POST'])
def update(item_id):
    try:
        item = Item.query.get(item_id)
        if not item:
            return "Item not found", 404

        if request.method == 'POST':
            item.name = request.form['item_name']
            with app.app_context():
                try:
                    db.session.commit()
                    print("Item updated successfully")
                except Exception as e:
                    print(f"Error updating item: {str(e)}")
            return redirect(url_for('index'))

        return render_template('update_crud.html', item=item)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return "Internal Server Error", 500

@app.route('/delete/<int:item_id>')
def delete(item_id):
    item = Item.query.get(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        try:
            db.create_all()
            print("Database created successfully")
        except Exception as e:
            print(f"Error creating database: {str(e)}")
    app.run(host="0.0.0.0", port=5002)
