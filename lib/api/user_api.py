import requests


# See API description on https://testbase.atlassian.net/wiki/spaces/USERS/pages/592511089
class UserAPI:

    def __init__(self):
        self.base_url = "http://users.bugred.ru/tasks/rest"
        self.create_user_with_tasks_endpoint = "/createuserwithtasks"
        self.add_avatar_endpoint = "/addavatar"
        self.delete_avatar_endpoint = "/deleteavatar"
        self._headers = {
            "Content-Type": "application/json"
        }
        # self._headers.update(some_bearer_token))

    def create_user_with_tasks(self, user):
        url = self.base_url + self.create_user_with_tasks_endpoint
        response = requests.post(
            url=url,
            json=user,
            headers=self._headers
        )
        assert response.status_code == 200
        assert "error" not in response.text, f"{response.text}"
        return response.json()

    def add_avatar(self, avatar_file, email):
        url = f"{self.base_url}{self.add_avatar_endpoint}/?email={email}"
        files = [
            ('avatar', ('kote.jpg', open(avatar_file, 'rb'), 'image/jpeg'))
        ]
        response = requests.post(
            url=url,
            files=files
        )
        assert response.status_code == 200
        assert "error" not in response.text, f"{response.text}"
        return response.json()

    def delete_avatar(self, email):
        url = f"{self.base_url}{self.delete_avatar_endpoint}/?email={email}"
        response = requests.delete(url=url)
        assert response.status_code == 200
        assert "error" not in response.text, f"{response.text}"
        return response.json()
