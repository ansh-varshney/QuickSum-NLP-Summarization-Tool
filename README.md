# QuikSum - Summarize Your Text Like a Boss!

QuikSum is a web application that provides quick and efficient text summarization using both extractive and abstractive methods. It supports multiple languages and includes sentiment analysis to give you deeper insights into your text. With a user-friendly interface, QuikSum makes it easy to summarize articles, documents, or any text input like a boss!

## 🚀 Features

- **Extractive Summarization**: Condenses text by extracting the most important sentences.
- **Abstractive Summarization**: Generates a summary using natural language processing to paraphrase the content.
- **Multilingual Support**: Summarize text in multiple languages.
- **Sentiment Analysis**: Analyze the sentiment of both the original text and the summary.
- **User-Friendly Interface**: Clean and modern design using Bootstrap for responsiveness.
- **Customizable Summary Length**: Specify the desired length of your summary.
- **Language Detection**: Automatically detects the language of the input text.

## 🛠️ Installation

### Prerequisites

- **Python 3.7 or higher**: Ensure Python is installed on your system.
- **Git**: For cloning the repository.

### Steps

1. **Clone the Repository**
2. **Create and Activate a Virtual Environment**
3. **Install Dependencies**: `pip install -r requirements.txt`
4. **Download NLTK Data**
5. **Run the Application**
6. **Access the Application**: Open your web browser and navigate to `http://127.0.0.1:5000/`.

## 📄 Usage

1. **Enter Text**

   Paste or type the text you want to summarize into the input field.

2. **Select Summarization Technique**

   - **Extractive**: Selects key sentences from the text.
   - **Abstractive**: Generates a summary in new words.

3. **Specify Summary Length (Optional)**

   - For **Extractive**: Enter a percentage (e.g., 30 for 30% of the original text).
   - For **Abstractive**: Enter the maximum number of tokens (e.g., 150).

4. **Specify Language (Optional)**

   - Enter the language code (e.g., `en` for English, `es` for Spanish).

5. **Click "Summarize"**

   - A loading spinner will appear while the summary is being generated.

6. **View Summary and Sentiment Analysis**

   - The summary will be displayed below the form.
   - Sentiment analysis results for both the original text and the summary will be shown.

## 🌐 Supported Languages

QuikSum supports multiple languages for both summarization and sentiment analysis. Language detection is automatic, but you can specify the language manually using ISO 639-1 codes.

## 🤖 Technologies Used

- **Python 3**
- **Flask**: Web framework.
- **NLTK**: Natural Language Toolkit for text processing.
- **Sumy**: Extractive summarization.
- **Transformers**: For abstractive summarization and sentiment analysis.
- **Hugging Face Models**:
  - `google/mt5-small` for multilingual abstractive summarization.
  - `nlptown/bert-base-multilingual-uncased-sentiment` for sentiment analysis.
- **Bootstrap 5**: Frontend framework for styling.
- **JavaScript (Fetch API)**: For asynchronous requests.

## 🐞 Troubleshooting

- **ModuleNotFoundError**: Ensure all dependencies are installed and the virtual environment is activated.
- **Model Download Issues**: Check your internet connection and verify that you have sufficient disk space.
- **Language Not Supported**: Not all languages may be supported. Check the language code or input text in a different language.

## 🙏 Acknowledgments

- **Hugging Face** for providing powerful NLP models.
- **NLTK and Sumy** for natural language processing tools.
- **Bootstrap** for the responsive UI components.
