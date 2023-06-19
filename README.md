# Mini Imdb Application: Movie Information, Recommendations, and Reviews Analysis

The Miniature IMDB Application is a Python-based application built using Streamlit. It allows users to search for movies, view detailed information about them, receive personalized content-based recommendations, and analyze sentiment in movie reviews. The application integrates various components such as the IMDB API, Latent Semantic Analysis (LSA), k-nearest neighbours (KNN), Selenium, TextBlob, and NLTK libraries.

# Table of Contents
- [Methodology](#methodology)
- [Features](#features)
- [Installation and Usage](#installation-and-usage)
- [Acknowledgements](#acknowledgements)

## Methodology
The Miniature IMDB Application follows a systematic methodology to provide users with movie information, recommendations, and sentiment analysis of movie reviews. The process begins with data ingestion, where movie data is read from a CSV file using the Pandas library. To ensure data completeness, missing director, cast, and country information is imputed using the IMDbPY library and web scraping, leveraging batch processing for efficiency.

After imputing missing data in the text, the data is cleaned by removing unnecessary characters, converting to lowercase, eliminating stopwords, and lemmatizing the words. Simultaneously, the movie data is prepared by encoding features for content-based analysis. The cleaned text data is then vectorized using the CountVectorizer, representing words as numerical vectors. The prepared movie data and vectorized text data form the foundation for building an accurate and effective recommendation system.

For movie recommendations, the application employs a content-based approach. Latent Semantic Analysis (LSA) is chosen to capture latent relationships and semantic meaning within the movie dataset. LSA helps identify similarities in movie content by analyzing the underlying structure of the data. It is particularly effective in uncovering hidden connections between movies based on their shared features and characteristics. The pre-computed data, including content similarity scores and the k-nearest neighbours (KNN) model, is loaded to enable efficient and accurate recommendations.

App development is carried out using the Streamlit library, which provides an intuitive user interface. Selenium and ChromeDriver are utilized for web scraping movie reviews from the IMDb website, ensuring up-to-date and comprehensive review data. The reviews are subjected to sentiment analysis using the TextBlob library and the Natural Language Toolkit (NLTK) SentimentIntensityAnalyzer. This analysis determines the sentiment polarity (positive, negative, or neutral) and subjectivity (subjective or objective) of the movie reviews.

## Features
1. Movie Information: Users can search for a specific movie and obtain detailed information about it. The application retrieves data from the IMDB API, including the title, cast, poster, plot, year of release, country, and genres. This feature allows users to quickly access comprehensive movie details in a user-friendly format.
2. Content-Based Recommendations: The application suggests a set of movie recommendations based on the content similarity of the searched movie. Leveraging Latent Semantic Analysis (LSA) and k-nearest neighbours (KNN), it identifies similar movies and presents them alongside their posters. This feature helps users discover new movies based on their interests and preferences.
3. Review Analysis: The application performs web scraping using Selenium to extract user reviews of the searched movie from the IMDB website. It collects review details such as the author, review date, rating, review title, and review text. The reviews are then subjected to sentiment analysis using the TextBlob library and the NLTK SentimentIntensityAnalyzer. This feature provides insights into the sentiment polarity (positive, negative, or neutral) and subjectivity (subjective or objective) of the movie reviews.
4. User-Friendly Interface: The app is built using the Streamlit library, which offers a user-friendly interface for seamless interaction. Users can easily search for movies, explore detailed information, view recommendations, and analyze reviews. The interface is designed to be intuitive and accessible to users of all levels of technical proficiency.

## Installation and Usage
1. Create a folder and open the terminal/command prompt in that directory
```
git clone https://github.com/roshancharlie/Mini-Imdb-Application.git
```
2.  Navigate to the project directory
```
cd path/folder/Mini-Imdb-Application
```
3. Install the required dependencies
```
pip install -r requirements.txt
```
4. Run the application
```
streamlit run app.py
```
## Acknowledgements
The Miniature IMDB Application utilizes the IMDB API, Streamlit, Selenium, TextBlob, NLTK, and other open-source libraries. We would like to express our gratitude to the developers of these libraries for their valuable contributions. If you encounter any issues or have any suggestions, please open an issue on the GitHub repository.
