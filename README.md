# Miniature IMDB Application
The Miniature IMDb Application is a web-based application that allows users to search for movies, view movie details, get recommendations, and analyze reviews. It provides a user-friendly interface for exploring movies and gaining insights into the sentiment of movie reviews.

## Features

- Movie Search: Users can search for a specific movie by selecting a movie title from the sidebar.
- Movie Details: The application retrieves detailed information about the selected movie, including the title, IMDb URL, cast, poster image, plot, year, country, and genres.
- Recommended Movies: The application suggests a list of movies similar to the selected movie based on content similarity. Users can discover new movies based on their preferences.
- Review Analysis: The application performs sentiment analysis on the reviews of the selected movie. It scrapes reviews from the IMDb website and displays each review with the author, review date, rating, review title, sentiment label (positive, negative, or objective), and subjective label (subjective or objective).
- IMDb-Inspired Design: The application features a custom CSS style inspired by IMDb's design. It provides an aesthetic and visually appealing interface for a better user experience.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/yourusername/miniature-imdb.git
   
   pip install -r requirements.txt
   
   streamlit run app.py
   
# Usage
1. Select a movie title from the sidebar to search for a specific movie.
2. The application will display detailed information about the selected movie, including its title, IMDb URL, cast, poster image, plot, year, country, and genres.
3. Explore the recommended movies section to discover similar movies based on the selected movie.
4. Analyze the sentiment of movie reviews in the review analysis section. Each review is displayed with its author, review date, rating, review title, sentiment label, and subjective label.
5. Enjoy exploring movies and gaining insights into their reviews!

# Customization
- CSS Styles: The application uses a custom CSS style inspired by IMDb's design. You can modify the CSS styles in the app.py file to customize the appearance of the application.
- Data Source: The application retrieves movie details from a data source. You can update the data source or integrate it with your own movie database by modifying the relevant functions in the app.py file.

# License
This project is licensed under the [Apache License](https://github.com/roshancharlie/Mini-Imdb-Application/blob/main/LICENSE)
