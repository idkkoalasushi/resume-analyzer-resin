from flask import send_from_directory
import os
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)
            return redirect(url_for('analysis'))
    return render_template('upload.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')  # Your file from earlier

if __name__ == '__main__':
    app.run(debug=True)

