from assertions.basic_assetions import assert_value
from clients.base_client import BaseClient
from clients.users.user_payload import get_user_payload
from util.api_helper import APIRequest


class DeleteUserClient(BaseClient):
    def __init__(self, token, id):
        super().__init__()
        self.url = f'{self.base_url}/users/{id}'
        self.api = APIRequest()
        self.headers = {"Authorization": f"Bearer {token}"}

    def delete_user(self):
        return self.api.delete(url=self.url, headers=self.headers)