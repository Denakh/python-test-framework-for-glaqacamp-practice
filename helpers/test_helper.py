import random
import string


def random_string(string_length=6):
    """Generate a random string of fixed length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(string_length))


def generate_token():
    return {"Authorization": f"Bearer {random_string()}"}
