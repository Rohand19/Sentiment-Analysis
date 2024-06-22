# app.py
import streamlit as st
from sentiment_analysis import analyze_sentiment, generate_explanation

st.title('Sentiment Analysis Chatbot')

user_input = st.text_area('Enter text:')

if st.button('Analyze'):
    sentiment, polarity, subjectivity = analyze_sentiment(user_input)
    explanation = generate_explanation(sentiment, polarity, subjectivity)
    st.subheader('Analysis Result')
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Polarity: {polarity:.2f}')
    st.write(f'Subjectivity: {subjectivity:.2f}')
    st.write(explanation)
