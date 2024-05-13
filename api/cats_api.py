import requests
from requests import Response


class CatsAPI:

    def __init__(self):
        self.url = "https://cat-fact.herokuapp.com/"
        self.headers = {
            'Content-Type': 'application/json'
        }

    def get_cat_facts(self) -> Response:
        """
        Method to get all cat facts

        :return: API's Response
        """
        resp = requests.get(url=f"{self.url}facts", headers=self.headers)
        return resp
