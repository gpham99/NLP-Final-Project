from flask import Flask, request
from io import BytesIO
from PyPDF2 import PdfReader
import torch
from transformers import BartTokenizer, BartForConditionalGeneration
from transformers import AutoTokenizer, AutoModelWithLMHead
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

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
    # T5 model names:
    # "hupd/hupd-t5-small"
    # "pszemraj/long-t5-tglobal-base-16384-book-summary"

    # T5 method outline (model name interchangeable):
    summarizer = pipeline(
    "summarization",
    "pszemraj/long-t5-tglobal-base-16384-book-summary",
    device=0 if torch.cuda.is_available() else -1,
    )
    summary = summarizer(text)
    return summary

    # Secondary T5 method:
    # tokenizer = AutoTokenizer.from_pretrained('t5-base')
    # model = AutoModelWithLMHead.from_pretrained('t5-base', return_dict=True)
    # inputs = tokenizer.encode("summarize: " + text, return_tensors='pt', max_length=512, truncation=True)
    # summary_ids = model.generate(inputs, max_length=100, min_length=80, length_penalty=5., num_beams=2)
    # summary = tokenizer.decode(summary_ids[0])
    # return summary

    # DistilBart method:
    # model = BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")
    # tokenizer = BartTokenizer.from_pretrained("facebook/bart-large-cnn")
    # inputs = tokenizer(text, max_length=1024, return_tensors = "pt")
    # summary_ids = model.generate(inputs["input_ids"], num_beams=2, min_length=0, max_length=20)
    # summary = tokenizer.batch_decode(summary_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    # return summary

    # NLTK TF IDF method:
    # stopWords = set(stopwords.words("english"))
    # words = word_tokenize(text)
    # freqTable = dict()
    # for word in words:
    #     word = word.lower()
    #     if word in stopWords:
    #         continue
    #     if word in freqTable:
    #         freqTable[word] += 1
    #     else:
    #         freqTable[word] = 1
    # sentences = sent_tokenize(text)
    # sentenceValue = dict() 
    # for sentence in sentences:
    #     for word, freq in freqTable.items():
    #         if word in sentence.lower():
    #             if word in sentence.lower():
    #                 if sentence in sentenceValue:
    #                     sentenceValue[sentence] += freq
    #                 else:
    #                     sentenceValue[sentence] = freq
    # sumValues = 0
    # for sentence in sentenceValue:
    #     sumValues += sentenceValue[sentence]
    # average = int(sumValues / len(sentenceValue))
    # summary = ""
    # for sentence in sentences:
    #     if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
    #         summary += " " + sentence
    # return summary
   

if __name__ == '__main__':
    app.run(debug=True)