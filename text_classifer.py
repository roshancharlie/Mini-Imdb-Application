# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:44:34 2023

@author: User
"""
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob

def preprocess_text(text):
    # Lowercase the text
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Remove numbers
    text = re.sub(r"\d+", "", text)

    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove stopwords
    stop_words = set(stopwords.words("english"))
    text = " ".join([word for word in text.split() if word not in stop_words])

    # Lemmatize the text
    lemmatizer = WordNetLemmatizer()
    text = " ".join([lemmatizer.lemmatize(word) for word in text.split()])

    return text

# Function to analyze sentiment
def analyze_sentiment(text):
    # Download the NLTK sentiment analysis package
    nltk.download('vader_lexicon')

    # Create an instance of the SentimentIntensityAnalyzer class
    analyzer = SentimentIntensityAnalyzer()

    # Analyze sentiment using the SentimentIntensityAnalyzer
    polarity = analyzer.polarity_scores(text)

    # Extract the sentiment scores
    compound_score = polarity['compound']

    # Determine the overall sentiment label
    if compound_score >= 0.05:
        sentiment_label = "Positive"
    elif compound_score <= -0.05:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"

    # Use TextBlob to calculate subjectivity
    blob = TextBlob(text)
    subjectivity = blob.sentiment.subjectivity

    # Determine the subjectivity label
    if subjectivity > 0.5:
        subjective_label = 'Subjective Comment'
    else:
        subjective_label = 'Objective Comment'

    # Return the sentiment label and subjective label
    return sentiment_label, subjective_label