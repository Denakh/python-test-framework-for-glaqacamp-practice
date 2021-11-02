from files import kote_jpg_path
from helpers.test_helper import random_string
from lib.api.user_api import UserAPI


class TestUser:

    @classmethod
    def setup_class(cls):
        cls.user_api = UserAPI()
        cls.user = {
            "email": f"{random_string()}@somemailservice.com",
            "name": random_string(),
            "tasks": [{
                "title": random_string(),
                "description": random_string()
            },
                {
                    "title": random_string(),
                    "description": random_string()
                }
            ]
        }

    def test_adding_and_deleting_for_new_user_is_successful(self):
        # given: created user
        user = self.user_api.create_user_with_tasks(self.user)

        # when: add avatar for the created user  python-test-framework-for-practice\files
        self.user_api.add_avatar(kote_jpg_path, user["email"])

        # and: delete the avatar
        response = self.user_api.delete_avatar(user["email"])

        # then: status of the last operation with avatar (delete) is "ok"
        assert response["status"] == "ok", "Status of the last operation (delete) isn't 'ok'"
