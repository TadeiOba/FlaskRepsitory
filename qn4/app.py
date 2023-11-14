from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678910'  # Replace with a secret key of your choice

class UserInputForm(FlaskForm):
    name = StringField('Name')
    age = StringField('Age')
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UserInputForm()

    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        return render_template('display.html', name=name, age=age)

    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5002)
