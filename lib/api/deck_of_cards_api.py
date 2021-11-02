import requests

DECK_OF_CARDS_API_ROOT_URL = "https://deckofcardsapi.com/api/deck/"


# See API description on https://deckofcardsapi.com/
class DeckOfCardsAPI:

    @staticmethod
    def shuffle_the_cards(deck_count: int):
        query_params = {
            "deck_count": deck_count
        }
        shuffle_the_cards_endpoint = "new/shuffle/"

        response = requests.get(DECK_OF_CARDS_API_ROOT_URL + shuffle_the_cards_endpoint, query_params)

        return {
            'response': response,
            'content': response.content,
            'headers': response.headers,
            'status_code': response.status_code
        }

    @staticmethod
    def create_brand_new_deck(contains_jokers: bool):
        query_params = {
            "jokers_enabled": contains_jokers
        }
        create_brand_new_deck_endpoint = "new/"

        response = requests.get(DECK_OF_CARDS_API_ROOT_URL + create_brand_new_deck_endpoint, query_params)

        return {
            'response': response,
            'content': response.content,
            'headers': response.headers,
            'status_code': response.status_code
        }
