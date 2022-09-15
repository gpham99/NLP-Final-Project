from flask import Flask, request
from io import BytesIO
from PyPDF2 import PdfReader

app = Flask(__name__)

@app.route('/members')
def index():
    return {"members": ["Mem 1", "Mem 2", "Mem 3"]}

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename != '':
            output = ""
            bytes_stream = BytesIO(f.read())
            pdfReader = PdfReader(bytes_stream)
            count = pdfReader.numPages
            for i in range(count):
                page = pdfReader.getPage(i)
                output += page.extractText()
        return output

if __name__ == '__main__':
    app.run(debug=True)