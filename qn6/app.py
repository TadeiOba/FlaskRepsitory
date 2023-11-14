from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = '12345678910'  # Replace with a secret key of your choice
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

class UploadForm(FlaskForm):
    file = FileField('Choose a file', validators=[
        FileRequired(),
        FileAllowed(app.config['ALLOWED_EXTENSIONS'], 'Invalid file type. Allowed types are txt, pdf, png, jpg, jpeg, gif.')
    ])

@app.route('/', methods=['GET', 'POST'])
def index():
    form = UploadForm()

    if form.validate_on_submit():
        file = form.file.data
        file.save(f'./{app.config["UPLOAD_FOLDER"]}/{file.filename}')
        return redirect(url_for('display', filename=file.filename))

    return render_template('index_upload.html', form=form)

@app.route('/display/<filename>')
def display(filename):
    return render_template('display_upload.html', filename=filename)

if __name__ == '__main__':
    app.run(host = "0.0.0.0",port = 5002)
