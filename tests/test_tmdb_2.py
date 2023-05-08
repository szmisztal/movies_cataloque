import pytest
from main import app
from unittest.mock import Mock

@pytest.mark.parametrize('list_type', [
    'popular',
    'now_playing',
    'top_rated',
    'upcoming',
    'latest'
])
def test_homepage(monkeypatch, list_type):
    api_mock = Mock(return_value = {'results': []})
    monkeypatch.setattr("tmdb_client.get_movies", api_mock)

    with app.test_client() as client:
        response = client.get(f'/?list_type={list_type}')
        assert response.status_code == 200
        api_mock.assert_called_once_with(how_many = 8, list_type = list_type)


