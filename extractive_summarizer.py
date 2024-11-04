# extractive_summarizer.py

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from sumy.utils import get_stop_words

def extractive_summarize(text, ratio=0.2, language='english'):
    try:
        parser = PlaintextParser.from_string(text, Tokenizer(language))
        summarizer = LexRankSummarizer()
        summarizer.stop_words = get_stop_words(language)
        # Calculate the number of sentences to include in the summary
        sentences_count = max(1, int(len(parser.document.sentences) * ratio))
        summary_sentences = summarizer(parser.document, sentences_count)
        summary = ' '.join([str(sentence) for sentence in summary_sentences])
        if not summary.strip():
            summary = "Unable to generate a summary with the given parameters."
    except Exception as e:
        summary = "Text is too short or language not supported for summarization."
    return summary
