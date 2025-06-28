import os
import mimetypes
from flask import Flask, request, send_from_directory, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'pdf', 'zip', 'docx'}

# Create upload folder if not exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part in request', 400
    file = request.files['file']
    if file.filename == '':
        return 'No file selected', 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Get metadata
        file_size = os.path.getsize(filepath)
        file_type = mimetypes.guess_type(filepath)[0]
        upload_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        download_url = url_for('download_file', filename=filename, _external=True)
        return render_template("success.html", filename=filename, file_size=f"{file_size / 1024:.2f} KB",
                               file_type=file_type, upload_time=upload_time, download_url=download_url)
    return 'Invalid file', 400

@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
