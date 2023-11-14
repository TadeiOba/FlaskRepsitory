from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678910'  # Replace with a secret key of your choice

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        name = request.form['name']
        age = request.form['age']

        # Store user data in the session
        session['name'] = name
        session['age'] = age

        return redirect(url_for('display'))

    return render_template('index_session.html')

@app.route('/display')
def display():
    # Retrieve user data from the session
    name = session.get('name', 'N/A')
    age = session.get('age', 'N/A')

    return render_template('display_session.html', name=name, age=age)

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5002)
