import streamlit as st
from text_classifer import preprocess_text,analyze_sentiment
from fetch import get_movie_details,get_poster
from scrapper import scrape_movie_reviews
from data import load_content_similarity,load_knn_model,load_movie_data


movie = load_movie_data()
content_similarity = load_content_similarity()
knn = load_knn_model()



def recommend_movies(movie_title, num_recommendations=5):
    # Find the index of the movie title
    movie_index = movie[movie['title'] == movie_title].index[0]

    # Get the indices of similar movies based on content similarity
    _, indices = knn.kneighbors([content_similarity[movie_index]], n_neighbors=num_recommendations+1)

    # Exclude the movie itself from recommendations
    indices = indices.squeeze()[1:]

    # Return the recommended movie titles
    recommended_movies = movie.iloc[indices]['title']
    return recommended_movies



# Main function to run the Streamlit app

def main():
    # Set custom CSS styles for IMDb-inspired design
    st.markdown(
        """
        <style>
        .title {
            font-size: 36px;
            font-weight: bold;
            color: #003580;
            text-align: center;
        }

        .subheader {
            font-size: 24px;
            font-weight: bold;
            color: #333333;
            margin-top: 20px;
        }

        .imdb-header {
            font-size: 24px;
            font-weight: bold;
            color: #003580;
            margin-top: 30px;
        }

        .poster {
            display: block;
            margin: 20px auto;
            max-width: 200px;  /* Adjust the max-width value as desired */
        }

        .review-author {
            font-size: 18px;
            font-weight: bold;
            margin-top: 20px;
        }

        .review-info {
            font-size: 14px;
            color: #666666;
            margin-bottom: 10px;
        }

        .review-sentiment {
            font-size: 16px;
            font-weight: bold;
            margin-top: 10px;
        }

        .positive {
            color: #008000;
        }

        .negative {
            color: #FF0000;
        }

        .objective {
            color: #333333;
        }

        .subjective {
            color: #666666;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h1 class='title'>Miniature IMDB Application</h1>", unsafe_allow_html=True)

    # Sidebar - Movie Title Slider
    movie_title = st.sidebar.selectbox("Select a Movie", options=movie['title'])

    # Sidebar - Search Button
    search_button = st.sidebar.button("Search")

    if search_button:
        movie_details = get_movie_details(movie_title)

        if movie_details:
            title, movie_url, cast, poster_url, plot, year, country, genres = movie_details

            # Display movie information
            st.markdown(f"<a href='{movie_url}' target='_blank'><h1 class='title'>{title}</h1></a>", unsafe_allow_html=True)
            
            # Poster
            st.image(poster_url, caption=title, use_column_width=True, output_format="JPEG")

            # Plot
            with st.expander("Plot", expanded=True):
                st.markdown(f"<p>{plot}</p>", unsafe_allow_html=True)

            # Year, Country, Genres
            with st.expander("Details", expanded=True):
                st.markdown(f"Year: {year}  \nCountry: {country}  \nGenres: {', '.join(genres)}", unsafe_allow_html=True)

            # Cast
            with st.expander("Cast", expanded=True):
                st.markdown(f"<p>{', '.join(cast)}</p>", unsafe_allow_html=True)

            st.header("Recommendation")
            recommended_movies = recommend_movies(movie_title, num_recommendations=5)

            # Display recommended movies side by side
            columns = st.columns(len(recommended_movies))
            for column, recommended_movie in zip(columns, recommended_movies):
                title, poster_url = get_poster(recommended_movie)
                with column:
                    st.markdown(f"<p class='imdb-header'>{recommended_movie}</p>", unsafe_allow_html=True)
                    if poster_url:
                        st.image(poster_url, caption=recommended_movie, use_column_width=True, output_format="JPEG")
                    else:
                        st.write("Poster URL not available for this movie.")

            st.header("Review Analysis")
            review_df = scrape_movie_reviews(movie_url)

            if not review_df.empty:
                for index, row in review_df.iterrows():
                    st.markdown(f"<p class='review-author'>Author: {row['Author']}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p class='review-info'>Review Date: {row['Review_Date']}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p class='review-info'>Rating: {row['Rating']}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p class='review-info'>Review Title: {row['Review_Title']}</p>", unsafe_allow_html=True)

                    # Preprocess and analyze sentiment of the review text
                    preprocessed_text = preprocess_text(row['Review'])
                    sentiment_label, subjective_label = analyze_sentiment(preprocessed_text)

                    # Set color based on sentiment label
                    if sentiment_label == 'Positive':
                        color = 'positive'
                    elif sentiment_label == 'Negative':
                        color = 'negative'
                    else:
                        color = 'objective'

                    # Set color for subjective label
                    if subjective_label == 'Subjective':
                        subjective_color = 'subjective'
                    else:
                        subjective_color = 'objective'

                    # Display sentiment label and subjective label
                    st.markdown(f"<p class='review-sentiment {color}'>Sentiment: {sentiment_label}</p>", unsafe_allow_html=True)
                    st.markdown(f"<p class='review-sentiment {subjective_color}'>{subjective_label}</p>", unsafe_allow_html=True)

                    st.write("Review: " + row['Review'])
                    st.write("--------------------------------------------------------------------")
            else:
                st.write("No reviews found for this movie.")
        else:
            st.write("Movie not found.")

if __name__ == "__main__":
    main()

