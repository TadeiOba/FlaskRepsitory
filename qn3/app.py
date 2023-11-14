from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, welcome to the dynamic content app!'

@app.route('/greet/<name>/<int:age>')
def greet(name, age):
    return render_template('home.html', name=name, age=age)

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5002)
