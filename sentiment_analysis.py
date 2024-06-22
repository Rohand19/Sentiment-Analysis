# sentiment_analysis.py
from textblob import TextBlob
import nltk

# Download NLTK data (if not already downloaded)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    sentiment = 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'
    return sentiment, polarity, subjectivity

def generate_explanation(sentiment, polarity, subjectivity):
    explanation = f"The sentiment of the text is {sentiment.lower()}.\n"
    if sentiment == 'Positive':
        explanation += f"It generally expresses a positive sentiment.\n"
    elif sentiment == 'Negative':
        explanation += f"It generally expresses a negative sentiment.\n"
    else:
        explanation += f"It is neutral in sentiment.\n"
    explanation += f"The polarity score is {polarity:.2f}, where a higher value indicates "
    explanation += f"more positive sentiment and a lower value indicates more negative sentiment.\n"
    explanation += f"The subjectivity score is {subjectivity:.2f}, where a higher value indicates "
    explanation += f"more subjective text and a lower value indicates more objective text."
    return explanation
