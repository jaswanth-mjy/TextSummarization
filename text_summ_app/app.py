# app.py
from flask import Flask, render_template, request
from summarization.text_summarizer import summarizer as text_summarizer
from summarization.youtube_transcript_summarizer import youtube_transcript_summarizer
from summarization.story_summarizer import story_summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('all_use_cases.html')

@app.route('/summarize_text', methods=['POST'])
def summarize_text():
    if request.method == 'POST':
        rawtext = request.form['input_text']
        text_summary = text_summarizer(rawtext)
    return render_template('all_use_cases.html', text_summary=text_summary)

@app.route('/summarize_youtube_transcript', methods=['POST'])
def summarize_youtube_transcript():
    if request.method == 'POST':
        rawtranscript = request.form['input_transcript']
        youtube_summary = youtube_transcript_summarizer(rawtranscript)
    return render_template('all_use_cases.html', youtube_summary=youtube_summary)

@app.route('/summarize_story', methods=['POST'])
def summarize_story():
    if request.method == 'POST':
        rawstory = request.form['input_story']
        story_summary = story_summarizer(rawstory)
    return render_template('all_use_cases.html', story_summary=story_summary)

if __name__ == '__main__':
    app.run(debug=True)
