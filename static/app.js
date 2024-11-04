// static/app.js

document.addEventListener('DOMContentLoaded', function() {
    // Initialize tooltips
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    var tooltipList = tooltipTriggerList.map(function (tooltipTrigger) {
        return new bootstrap.Tooltip(tooltipTrigger)
    });
});

document.getElementById('summarize-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const text = document.getElementById('text').value.trim();
    const technique = document.getElementById('technique').value;
    const lengthInput = document.getElementById('length').value.trim();
    const languageInput = document.getElementById('language').value.trim();
    let length = null;

    if (lengthInput) {
        length = parseInt(lengthInput);
        if (isNaN(length) || length <= 0) {
            alert('Please enter a valid number for summary length.');
            return;
        }
    }

    if (!text) {
        alert('Please enter text to summarize.');
        return;
    }

    // Clear previous summary and sentiment, and show loader
    document.getElementById('summary-text').innerHTML = '<div class="loader"></div>';
    document.getElementById('sentiment-text').innerHTML = '';

    // Prepare data to send
    const data = { text, technique };
    if (length) {
        data.length = length;
    }
    if (languageInput) {
        data.language = languageInput;
    }

    // Send POST request to backend
    fetch('/summarize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            return response.json().then(errData => { throw errData; });
        }
        return response.json();
    })
    .then(data => {
        if (data.summary) {
            document.getElementById('summary-text').innerText = data.summary;

            // Display sentiment analysis results
            const sentiment = data.sentiment;
            const summarySentiment = data.summary_sentiment;

            document.getElementById('sentiment-text').innerHTML = `
                <p><strong>Original Text Sentiment:</strong> ${sentiment.label} (${(sentiment.score * 100).toFixed(2)}%)</p>
                <p><strong>Summary Sentiment:</strong> ${summarySentiment.label} (${(summarySentiment.score * 100).toFixed(2)}%)</p>
            `;
        } else if (data.error) {
            document.getElementById('summary-text').innerHTML = '<div class="alert alert-danger">' + data.error + '</div>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('summary-text').innerHTML = '<div class="alert alert-danger">An error occurred during summarization.</div>';
    });
});
