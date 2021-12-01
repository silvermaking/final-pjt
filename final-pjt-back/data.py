from pprint import pprint
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'finalpjt.settings')

import django
django.setup()

import requests

from movies.models import Genre, Movie

import json
# from decouple import config

apikey = '37d1290f9ce8f25ac7dbd0039512f80a'
lang = 'ko-KR'
page = 1
region = 'KR'

# genre_url = f'https://api.themoviedb.org/3/genre/movie/list?api_key={apikey}&language={lang}'
# genre_response = requests.get(genre_url).json().get('genres')

# print(genre_response)

# for name in genre_response:
#     genre = Genre()
#     genre.id = name['id']
#     genre.genre = name['name']
#     genre.save()

for i in range(1,2):
    movie_url = f'https://api.themoviedb.org/3/movie/popular?api_key={apikey}&language=ko&page={i}'
    movie_response = requests.get(movie_url).json().get('results')
    # pprint(movie_response)
    for name in movie_response:
       
        movie = Movie()
        movie.movie_no = name['id']
        movie.title = name['title']
        movie.release_date = name['release_date']
        movie.poster_path = name['poster_path']
        movie.adult = name['adult']
        movie.rate = name['vote_average']
        movie.overview = name['overview']
        movie.vote_count = name['vote_count']

        movie.save()
        for genre in movie['genres']:
            movie.genres.add(genre)