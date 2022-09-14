from flask import Flask, request
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/members')
def index():
    return {"members": ["Mem 1", "Mem 2", "Mem 3"]}

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename != '':
            f.save(secure_filename(f.filename))
        return 'file uploaded successfully'

if __name__ == '__main__':
    app.run(debug=True)