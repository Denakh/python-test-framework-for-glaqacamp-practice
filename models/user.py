from helpers.test_helper import random_string


class User:
    def __init__(self, tasks):
        self.user = random_string()
        self.date_updated = None
        self.role = None
        self.date_register = None
        self.date = None
        self.email = f"{random_string()}@somemailservice.com"
        self.by_user = None
        self.companies = None
        self.tasks = tasks
