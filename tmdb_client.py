import requests

import random

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiODUzMmY5MGFlZTFjMzdiMmNiYTJkZjk5YjJkMGI2NiIsInN1YiI6IjY0MmQzYjYwNjQ3NjU0MDBmMmJlMGViZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.M3uwqm2res2Xc8DhA40IDWR6luqMH0C4bC4G9khdmE8"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers = headers)
    return response.json()

def get_movies(how_many):
    data = get_popular_movies()["results"]
    random.shuffle(data)
    return data[:how_many]

def get_poster_url(poster_api_path, size = "w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"


