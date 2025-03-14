# 🎭 Sentiment Analysis Chatbot

[![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io/)
[![TextBlob](https://img.shields.io/badge/TextBlob-0.15+-green.svg)](https://textblob.readthedocs.io/)
[![NLTK](https://img.shields.io/badge/NLTK-3.5+-orange.svg)](https://www.nltk.org/)

<div align="center">
  <img src="https://raw.githubusercontent.com/ushmidave/readme-assets/main/sentiment-analysis.png" alt="Sentiment Analysis" width="500"/>
</div>

## 📑 Overview

The Sentiment Analysis Chatbot is an interactive web application that analyzes the emotional tone of text inputs. It provides users with insights about whether a given text expresses positive, negative, or neutral sentiment, along with polarity and subjectivity scores.

## ✨ Features

- **Real-time Sentiment Analysis**: Instantly analyze the sentiment of any text input
- **Detailed Metrics**: Get polarity and subjectivity scores along with sentiment classification
- **Insightful Explanations**: Receive human-readable explanations of analysis results
- **User-friendly Interface**: Clean and intuitive web interface powered by Streamlit

## 🔧 Technologies

- **Python**: Core programming language
- **Streamlit**: Interactive web application framework
- **TextBlob**: Natural Language Processing (NLP) library for sentiment analysis
- **NLTK**: Comprehensive natural language toolkit

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Access the application**
   - Open your browser and go to `http://localhost:8501`

## 💻 Usage

1. Enter or paste text in the input area
2. Click the "Analyze" button
3. View the sentiment analysis results:
   - Overall sentiment (Positive, Negative, or Neutral)
   - Polarity score (-1 to 1, where -1 is very negative and 1 is very positive)
   - Subjectivity score (0 to 1, where 0 is objective and 1 is subjective)
   - A detailed explanation of the results

## 🔍 How It Works

The application uses TextBlob, a Python library for processing textual data, to perform sentiment analysis:

1. The user input is processed using TextBlob's sentiment analysis capabilities
2. TextBlob returns polarity and subjectivity scores
3. Based on the polarity score, the text is classified as Positive, Negative, or Neutral
4. A human-readable explanation is generated to help interpret the results

## 📊 Example Results

| Input Text | Sentiment | Polarity | Subjectivity |
|------------|-----------|----------|--------------|
| "I love this product! It's amazing." | Positive | 0.8 | 0.75 |
| "This is absolutely terrible service." | Negative | -0.7 | 0.6 |
| "The meeting is scheduled for tomorrow." | Neutral | 0.0 | 0.0 |

## 🛠️ Project Structure

```
sentiment-analysis/
├── app.py                 # Main Streamlit application
├── sentiment_analysis.py  # Core sentiment analysis functionality
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```

## 🔮 Future Enhancements

- Add support for multiple languages
- Implement more advanced NLP techniques for better accuracy
- Create visualization dashboards for sentiment trends
- Add ability to analyze sentiment from URLs or file uploads
- Integrate with social media APIs for real-time sentiment monitoring

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👥 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

<div align="center">
  <p>Developed with ❤️ for natural language understanding</p>
</div> 