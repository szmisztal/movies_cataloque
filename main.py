from flask import Flask, url_for, request, render_template, redirect, flash
import random
import datetime
import tmdb_client

favorites = ()

app = Flask(__name__)

app.secret_key = b'secret_key'

@app.route('/')
def homepage():
    list_types = ['popular', 'now_playing', 'top_rated', 'upcoming', 'latest']
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in list_types:
        selected_list = 'popular'
    movies = tmdb_client.get_movies(how_many = 8, list_type = selected_list)
    return render_template("homepage.html", movies = movies, current_list = selected_list, list_types = list_types)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    movie_images = tmdb_client.get_movie_images(movie_id)
    selected_backdrop = random.choice(movie_images["backdrops"])
    return render_template("movie_details.html", movie = details, cast = cast, backdrop = selected_backdrop)

@app.route('/search')
def search():
    search_query = request.args.get("q", "")
    if search_query:
        movies = tmdb_client.search(search_query = search_query)
    else:
        movies = []
    return render_template("search.html", movies = movies, search_query = search_query)

@app.route('/today')
def today():
    movies = tmdb_client.get_airing_today()
    today = datetime.date.today()
    return render_template("today.html", movies = movies, today = today)

@app.route("/favorites/add", methods=['POST'])
def add_to_favorites():
    data = request.form
    movie_id = data.get('movie_id')
    movie_title = data.get('movie_title')
    if movie_id and movie_title:
        favorites.add(movie_id)
        flash(f'Movie added {movie_title} to favorites !')
    return redirect(url_for('homepage'))

@app.route("/favorites")
def show_favorites():
    if favorites:
        movies = []
        for movie_id in favorites:
            movie_details = tmdb_client.get_single_movie(movie_id)
            movies.append(movie_details)
    else:
        movies = []
    return render_template("homepage.html", movies = movies)

if __name__ == '__main__':
    app.run(debug = True)
