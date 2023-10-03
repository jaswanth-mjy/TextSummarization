# app.py
from flask import Flask, render_template, request
from text_summary import summarizer, youtube_transcript_summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary, original_txt, len_orig, len_summary = summarizer(rawtext)
    return render_template('summary.html', summary=summary, original_txt=original_txt, len_orig=len_orig, len_summary=len_summary)

@app.route('/analyze_youtube', methods=['GET', 'POST'])
def analyze_youtube():
    if request.method == 'POST':
        rawtranscript = request.form['rawtranscript']
        summary = youtube_transcript_summarizer(rawtranscript)
    return render_template('youtube_summary.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
