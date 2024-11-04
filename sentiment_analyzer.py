# sentiment_analyzer.py

from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the sentiment analysis model and tokenizer once at startup
sentiment_model_name = 'nlptown/bert-base-multilingual-uncased-sentiment'
sentiment_tokenizer = AutoTokenizer.from_pretrained(sentiment_model_name)
sentiment_model = AutoModelForSequenceClassification.from_pretrained(sentiment_model_name)

def analyze_sentiment(text, language='en'):
    # Tokenize the input text
    inputs = sentiment_tokenizer.encode_plus(
        text,
        return_tensors='pt',
        truncation=True,
        max_length=512
    )

    # Get model predictions
    outputs = sentiment_model(**inputs)
    scores = outputs[0][0].detach().numpy()
    scores = torch.nn.functional.softmax(torch.tensor(scores), dim=0).numpy()

    # The model outputs scores for ratings from 1 to 5
    labels = ['Very Negative', 'Negative', 'Neutral', 'Positive', 'Very Positive']
    sentiment = {
        'label': labels[scores.argmax()],
        'score': float(scores.max())
    }

    return sentiment
