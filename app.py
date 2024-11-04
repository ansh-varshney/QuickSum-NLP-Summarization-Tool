# app.py

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from extractive_summarizer import extractive_summarize
from abstractive_summarizer import abstractive_summarize
from sentiment_analyzer import analyze_sentiment
from langdetect import detect

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('text', '')
    technique = data.get('technique', 'extractive')
    length = data.get('length', None)

    if not text:
        return jsonify({'error': 'No text provided.'}), 400

    # Detect language
    try:
        language = detect(text)
    except Exception as e:
        return jsonify({'error': 'Language detection failed.'}), 400

    # Perform sentiment analysis
    sentiment = analyze_sentiment(text, language)

    if technique == 'extractive':
        # Use length as ratio (percentage of original text)
        if length:
            ratio = float(length) / 100.0  # Convert percentage to decimal
            # Ensure ratio is between 0.01 and 0.99
            ratio = max(0.01, min(ratio, 0.99))
        else:
            ratio = 0.2  # Default ratio
        summary = extractive_summarize(text, ratio=ratio, language=language)
    elif technique == 'abstractive':
        # Use length as max_length (number of tokens)
        if length:
            max_length = int(length)
            min_length = max_length // 2  # Set min_length to half of max_length
        else:
            max_length = 150
            min_length = 40
        summary = abstractive_summarize(text, max_length=max_length, min_length=min_length, language=language)
    else:
        return jsonify({'error': 'Invalid summarization technique.'}), 400

    # Analyze sentiment of the summary
    summary_sentiment = analyze_sentiment(summary, language)

    return jsonify({
        'summary': summary,
        'sentiment': sentiment,
        'summary_sentiment': summary_sentiment
    })

if __name__ == '__main__':
    app.run(debug=True)
