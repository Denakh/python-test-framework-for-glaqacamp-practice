import json

from lib.api.deck_of_cards_api import DeckOfCardsAPI


class TestDeckOfCards:

    # @classmethod
    # def setup_class(cls):
    #     cls.deck_of_cards_api = DeckOfCardsAPI()

    def test_shuffle_cards_for_2_decks(self):
        # Shuffle cards for 2 decks
        response = DeckOfCardsAPI.shuffle_the_cards(2)
        response_content = json.loads(response["content"])

        # Check deck number is 2 in the response (number of cards is 104)
        assert response_content["remaining"] == 104, \
            f"Actual number of cards ({response['content']['remaining']}) doesn't comply with 2 decks (104 cards)"

    def test_create_brand_new_deck_with_jokers(self):
        # Create a new deck with jokers
        response = DeckOfCardsAPI.create_brand_new_deck(True)
        response_content = json.loads(response["content"])

        # Check number of cards is 54 (with 2 jokers)
        assert response_content["remaining"] == 54, \
            f"Actual number of cards ({response['content']['remaining']}) doesn't contain 2 jokers decks (54 cards)"
