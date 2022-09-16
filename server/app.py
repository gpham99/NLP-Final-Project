from flask import Flask, request
from io import BytesIO
from PyPDF2 import PdfReader
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead

app = Flask(__name__)

@app.route('/members')
def index():
    return {"members": ["Mem 1", "Mem 2", "Mem 3"]}

@app.route('/upload', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        if f.filename != '':
            bytes_stream = BytesIO(f.read())
            pdfReader = PdfReader(bytes_stream)
            count = pdfReader.numPages
            summary = ""
            for i in range(count):
                page = pdfReader.getPage(i)
                output = page.extractText()
                page_summary = str(summarize(output))
                summary = summary + page_summary + "\n" + "\n"
        return summary

def summarize(text):
    # summarizer = pipeline(
    # "summarization",
    # "pszemraj/long-t5-tglobal-base-16384-book-summary",
    # device=0 if torch.cuda.is_available() else -1,
    # )
    # result = summarizer(text)
    # return result
    tokenizer = AutoTokenizer.from_pretrained('t5-base')
    model = AutoModelWithLMHead.from_pretrained('t5-base', return_dict=True)
    inputs = tokenizer.encode("summarize: " + text, return_tensors='pt', max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=100, min_length=80, length_penalty=5., num_beams=2)
    summary = tokenizer.decode(summary_ids[0])
    return summary
    
if __name__ == '__main__':
    app.run(debug=True)