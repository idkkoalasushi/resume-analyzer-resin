from flask import Flask, render_template

app = Flask(__name__)

@app.route('/analysis')
def analysis():
    # Example data, replace with your actual scanned result list
    scanned_result = [
        # Each item: [sentence, tag1, tag2, ...]
        ["Implemented feature X with 20% efficiency gain", "Metrics", "Actionable", "Domain-Specific"],
        ["Worked on UI design", "Actionable"],
        ["Improved server speed", "Metrics"],
        # Add more as needed
    ]

    # Example number of PNG pages to display
    num_pages = 3

    return render_template('analysis.html', scanned_result=scanned_result, num_pages=num_pages)

if __name__ == '__main__':
    app.run(debug=True)
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

