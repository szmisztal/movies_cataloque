import requests
import random

api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJiODUzMmY5MGFlZTFjMzdiMmNiYTJkZjk5YjJkMGI2NiIsInN1YiI6IjY0MmQzYjYwNjQ3NjU0MDBmMmJlMGViZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.M3uwqm2res2Xc8DhA40IDWR6luqMH0C4bC4G9khdmE8"

def call_tmdb_api(endpoint):
   full_url = f"https://api.themoviedb.org/3/{endpoint}"
   headers = {
       "Authorization": f"Bearer {api_token}"
   }
   response = requests.get(full_url, headers = headers)
   response.raise_for_status()
   return response.json()
def get_movies_list(list_type = 'popular'):
   return call_tmdb_api(f"movie/{list_type}")

def get_movies(how_many, list_type):
    data = get_movies_list()["results"]
    random.shuffle(data)
    return data[:how_many]

def get_poster_url(poster_api_path, size = "w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_single_movie(movie_id):
    return call_tmdb_api(f"/movie/{movie_id}")

def get_single_movie_cast(movie_id):
    movie_credits = call_tmdb_api(f"/movie/{movie_id}/credits")
    return movie_credits['cast']

def get_movie_images(movie_id):
    return call_tmdb_api(f"/movie/{movie_id}/images")

def search(search_query):
    search_movie = call_tmdb_api(f"/search/movie?query={search_query}")
    return search_movie['results']

def get_airing_today():
    air_today = call_tmdb_api(f"/tv/airing_today")
    return air_today['results']

