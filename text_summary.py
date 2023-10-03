from heapq import nlargest
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

text ="""LLaMA comes in four size variants: 7B, 13B, 33B, and 65B parameters. The paper shows that training smaller foundation models on large enough tokens is desirable, as it requires less computing power and resources. The 65B parameter models have been trained on 1.4 trillion tokens, while the LLaMA 7B model has been trained on 1 trillion tokens.

Just a few weeks after the release of LLaMA, the open-source community embraced it by creating an optimized version and expanding its use cases. Now, you can fine-tune LLaMA using LoRA (reduces the number of trainable parameters for fine-tuning) and train a chatbot with Stanford Alpaca.

Lightning AI has also joined the trend by providing an open-source, from-scratch rewrite of LLaMA called Lit-LLaMA. The main highlight of Lit-LLaMA is that it is released under the Apache 2.0 license, which makes it easier to adopt for other deep learning projects that use similar permissive licenses and also enables commercial use. It has scripts for optimized training and fine-tuning with LoRA."""
def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    #print(stopwords)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    #print(doc)

    token = [token.text for token in doc]
    #print(token)
    
    # Below for loop checks and finds word frequency dictionary and makes a count for each word 
    word_freq = {}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
    #print(word_freq)

    max_freq = max(word_freq.values())
    #print(max_freq)

    for word in word_freq.keys():
        word_freq[word] = word_freq[word] / max_freq
    #print(word_freq)

    sent_tokens = [sent for sent in doc.sents]
    #print(sent_tokens)

    sent_scores = {}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]
    #print(sent_scores)

    select_len = int(len(sent_tokens) * 0.3)
    #print(select_len)
    summary = nlargest(select_len, sent_scores, key=sent_scores.get)
    #print(summary)
    final_summary = {word.text for word in summary}
    summary = ' '.join(final_summary)
    #print(text)
    #print(summary)
    #print("Length of original text", len(text.split(' ')))
    #print("Length of summary text", len(summary.split(' ')))
    return summary, doc, len(rawdocs.split(' ')), len(summary. split(' '))