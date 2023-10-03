from transformers import pipeline

def story_summarizer(raw_story):
    summarization_pipeline = pipeline("summarization")
    summary = summarization_pipeline(raw_story, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    return summary
