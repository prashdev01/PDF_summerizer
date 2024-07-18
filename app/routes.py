from flask import render_template, request
from app import app
from app.summarizer import extract_text_from_pdf, summarize_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        text = extract_text_from_pdf(file)
        summary = summarize_text(text)
        return render_template('result.html', summary=summary)
    return render_template('index.html')
