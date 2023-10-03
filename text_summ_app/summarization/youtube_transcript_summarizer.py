from transformers import pipeline

def youtube_transcript_summarizer(raw_transcript):
    summarization_pipeline = pipeline("summarization")
    summary = summarization_pipeline(raw_transcript, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return summary
