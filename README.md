# File Sharing Web App
A simple, secure, and efficient file-sharing web application built with Flask and Python, allowing users to upload and download files with ease.

 Features:
- Upload any type of file (PDF, ZIP, DOCX, PNG, etc.)
- Download files from a central file list
- Auto-delete feature for expired/unused files (optional)
- Clean UI with Bootstrap for professional look
- Stores files securely in a local uploads/ folder or cloud-ready (S3 integration ready)

Tech Stack:
- Python 3.10+
- Flask — Web framework
- Flask-Uploads / werkzeug — File handling
- Bootstrap 5 — Frontend design

Sample Workflow:
- Upload a file using the form.
- File appears in the shared file list.
- Anyone can download by clicking "Download".
- Optional: Files auto-delete after X minutes/hours (feature-ready).

Future Enhancements:
- User authentication for private file sharing
- Auto-expiry for time-limited links
- Cloud storage (AWS S3 / Firebase)
- File-sharing link via email

Author:
Deeraj Ganesh M
