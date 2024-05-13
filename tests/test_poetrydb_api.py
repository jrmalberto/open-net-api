import pytest

from api.poetrydb_api import PoetryDBAPI
from pytest_assume.plugin import assume

class TestPoetryDBAPI:
    adams_title = "A Song of Autumn"

    @pytest.mark.parametrize("author", ["Adam Lindsay Gordon"])
    def test_get_authors(self, author):
        """
        Test to simulate verifying if author exists after being inserted
        """

        a = PoetryDBAPI()
        resp = a.get_authors()

        with assume:
            assert resp.status_code == 200, "Wrong status code returned"
        with assume:
            assert author in resp.json().get("authors"), "API response does not include the author"

    @pytest.mark.parametrize("title", ["A Song of Autumn", "An Exile's Farewell"])
    def test_author_tile(self, title):
        """
        Test to simulate verifying if title exists after being inserted for specific author
        """
        a = PoetryDBAPI()
        resp = a.get_author_titles("Adam Lindsay Gordon")

        with assume:
            assert resp.status_code == 200, "Wrong status code returned"
        existing_titles = []
        for t in resp.json():
            existing_titles.append(t.get("title"))
        with assume:
            assert title in existing_titles, "API response does not include the titles from specific author"

    @pytest.mark.skip("Currently bugged, status code != 404 like in response json")
    def test_negative_author_title(self):
        """
        Negative test response when using a not existing author
        """
        a = PoetryDBAPI()
        resp = a.get_author_titles("random")
        with assume:
            assert resp.status_code == resp.json().get("status"), "Wrong status code returned"
