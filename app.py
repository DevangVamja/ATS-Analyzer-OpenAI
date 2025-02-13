# FLASK APP - Run the app using flask --app app.py run
import os, sys, json
from pypdf import PdfReader 
from flask import Flask, request, render_template
from _parser import extractor

sys.path.insert(0, os.path.abspath(os.getcwd()))


UPLOAD_PATH = r"__data__"
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/upload", methods=["POST"])
def ats():
    file = request.files['pdf_doc']
    file.save(os.path.join(UPLOAD_PATH, "file.pdf"))
    file_path = os.path.join(UPLOAD_PATH, "file.pdf")
    data = __read_file__(file_path)
    data = extractor(data)

    return render_template('index.html', data = json.loads(data))
 
def __read_file__(path):
    reader = PdfReader(path) 
    data = ""

    for page_no in range(len(reader.pages)):
        page = reader.pages[page_no] 
        data += page.extract_text()

    return data 


if __name__ == "__main__":
    app.run(port=5000, debug=False)
