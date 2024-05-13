from pytest_assume.plugin import assume

from api.cats_api import CatsAPI


class TestCatsAPI:

    def test_cat_facts(self):
        """
        Verify API's get method works and returns expected results
        """
        cats_api = CatsAPI()

        facts_resp = cats_api.get_cat_facts()

        # Make sure we receive the correct status code in the response
        with assume:
            assert facts_resp.status_code == 200, "Wrong status code returned"
        # Verify expected text for a specific entry
        with assume:
            assert facts_resp.json()[0].get("text") == "Owning a cat can reduce the risk of stroke and heart attack by a third.", \
            "Cat fact with wrong text"

