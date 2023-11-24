from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import flash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Book model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)


# Routes

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        new_book = Book(title=title, author=author)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    book = Book.query.get(id)
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', book=book)

@app.route('/delete/<int:id>')
def delete(id):
    book = Book.query.get(id)
    db.session.delete(book)
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
