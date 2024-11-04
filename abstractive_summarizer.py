# abstractive_summarizer.py

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# Load the multilingual tokenizer and model once at startup
tokenizer = AutoTokenizer.from_pretrained('google/mt5-small')
model = AutoModelForSeq2SeqLM.from_pretrained('google/mt5-small')

def abstractive_summarize(text, max_length=150, min_length=40, language='en'):
    # Prepare the text input
    input_text = 'summarize: ' + text.strip().replace("\n", " ")

    # Tokenize the input text
    inputs = tokenizer.encode(input_text, return_tensors='pt', truncation=True, max_length=512)

    # Generate the summary
    summary_ids = model.generate(
        inputs,
        max_length=max_length,
        min_length=min_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True,
        no_repeat_ngram_size=3
    )

    # Decode and return the summary
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary
