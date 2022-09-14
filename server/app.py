from flask import Flask, request
from werkzeug.utils import secure_filename
import PyPDF2

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
        # The following opens the PDF file and reads the text page by page, adding each to the output string.
        pdfFileObj = open(f.filename, 'rb')
        output = ""
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        count = pdfReader.numPages
        for i in range(count):
            page = pdfReader.getPage(i)
            output += page.extractText()
        pdfFileObj.close()
        return output

if __name__ == '__main__':
    app.run(debug=True)