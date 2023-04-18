import requests
import random

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiODUzMmY5MGFlZTFjMzdiMmNiYTJkZjk5YjJkMGI2NiIsInN1YiI6IjY0MmQzYjYwNjQ3NjU0MDBmMmJlMGViZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.M3uwqm2res2Xc8DhA40IDWR6luqMH0C4bC4G9khdmE8"

def get_movies_list(list_type = "popular"):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies(how_many, list_type):
    data = get_movies_list()["results"]
    random.shuffle(data)
    return data[:how_many]

def get_poster_url(poster_api_path, size = "w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers = headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers = headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers = headers)
    return response.json()

def search(search_query):
   endpoint = f"https://api.themoviedb.org/3/search/movie?query={search_query}"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   response = requests.get(endpoint, headers = headers)
   response = response.json()
   return response['results']

def get_airing_today():
    endpoint = f"https://api.themoviedb.org/3/tv/airing_today"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers = headers)
    response.raise_for_status()
    response = response.json()
    return response['results']
