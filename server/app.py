from flask import Flask

app = Flask(__name__)

@app.route('/members')
def index():
    return {"members": ["Mem 1", "Mem 2", "Mem 3"]}

if __name__ == '__main__':
    app.run(debug=True)