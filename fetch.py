# -*- coding: utf-8 -*-
"""
Created on Thu Jun  1 18:34:54 2023

@author: User
"""

from imdb import IMDb

def get_movie_details(movie_title):
    # Create an instance of the IMDb class
    ia = IMDb()

    # Search for movies with the given title
    movies = ia.search_movie(movie_title)

    if movies:
        movie = movies[0]
        ia.update(movie)

        # Retrieve movie details
        title = movie['title']
        movie_url = ia.get_imdbURL(movie)
        cast = [actor['name'] for actor in movie['cast'][:10]]  # Get only the first 10 cast members
        poster_url = movie['full-size cover url']
        plot = movie['plot'][0]
        year = movie['year']
        country = movie['countries'][0]
        genres = movie['genres']

        return title, movie_url, cast, poster_url, plot, year, country, genres
    else:
        return None
def get_poster(movie_title):
    # Create an instance of the IMDb class
    ia = IMDb()

    # Search for movies with the given title
    movies = ia.search_movie(movie_title)

    if movies:
        movie = movies[0]
        ia.update(movie)

        # Retrieve movie details
        title = movie['title']
        poster_url = movie['full-size cover url']

        return title, poster_url
    else:
        return None