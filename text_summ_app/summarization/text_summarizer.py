from transformers import pipeline

def summarizer(rawtext):
    summarization_pipeline = pipeline("summarization")
    summary = summarization_pipeline(rawtext, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return summary
