## Handwritten Digit Recognition System
## By Sundas Noreen and Sayeda Asma

from flask import Flask, request, redirect, url_for,render_template
import os

UPLOAD_FOLDER = "static/img/"
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
SECRET_KEY = os.urandom(12)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods =["GET", "POST"])
def home():
    if request.method == 'POST':
        file = request.files['fileup']
        if file and allowed_file(file.filename):
            filename = "word.png"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print("Done")
            return redirect(url_for("result"))
    return render_template('upload.html')
from main import infermain
@app.route('/result')
def result():
    myresult=infermain()
    print(myresult)
    return render_template('index.html',myresult=myresult)

if __name__ == '__main__':
    app.run(debug=True)
