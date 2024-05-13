import requests


class PoetryDBAPI:

    def __init__(self):
        self.url = "https://poetrydb.org/"
        self.headers = {
            'Content-Type': 'application/json'
        }

    def get_authors(self):
        """
        Method to get all authors

        :return: API's Response
        """
        resp = requests.get(url=f"{self.url}author", headers=self.headers)
        return resp

    def get_author_titles(self, author_name):
        """
        Method to get all titles from a specific author

        :param author_name: Author name to search titles of
        :return: API's response
        """
        resp = requests.get(url=f"{self.url}author/{author_name}/title", headers=self.headers)
        return resp