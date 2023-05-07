from unittest.mock import Mock
import tmdb_client

def test_get_poster_url_uses_default_size():
    poster_api_path = "some-poster-path"
    expected_url = "https://image.tmdb.org/t/p/w342/some-poster-path"
    poster_url = tmdb_client.get_poster_url(poster_api_path = poster_api_path)
    assert poster_url == expected_url

def test_get_movies_list(monkeypatch):
    mock_list_type = "list_type"
    mock_movies_list = ['Movie 1', 'Movie 2']
    mock_call_tmdb_api = Mock(return_value = mock_movies_list)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", mock_call_tmdb_api)
    movies_list = tmdb_client.get_movies_list(list_type = mock_list_type)
    assert movies_list == mock_movies_list

def test_get_single_movie(monkeypatch):
    mock_movie_id = 123
    mock_single_movie = {'title': 'Movie 1'}
    mock_call_tmdb_api = Mock(return_value = mock_single_movie)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", mock_call_tmdb_api)
    single_movie = tmdb_client.get_single_movie(movie_id = mock_movie_id)
    assert single_movie == mock_single_movie

def test_get_movie_images(monkeypatch):
    mock_movie_id = 123
    mock_movie_images = {'images': ['Image 1', 'Image 2']}
    mock_call_tmdb_api = Mock(return_value = mock_movie_images)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", mock_call_tmdb_api)
    movie_images = tmdb_client.get_movie_images(movie_id = mock_movie_id)
    assert movie_images == mock_movie_images

def test_get_single_movie_cast(monkeypatch):
    mock_movie_id = 123
    mock_movie_cast = {'cast': ['Actor 1', 'Actor 2']}
    mock_call_tmdb_api = Mock(return_value = mock_movie_cast)
    monkeypatch.setattr("tmdb_client.call_tmdb_api", mock_call_tmdb_api)
    movie_cast = tmdb_client.get_single_movie_cast(movie_id = mock_movie_id)
    assert movie_cast == mock_movie_cast['cast']
