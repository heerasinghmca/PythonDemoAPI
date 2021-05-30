from assertions.basic_assetions import assert_value
from clients.base_client import BaseClient
from clients.users.user_payload import get_user_payload
from util.api_helper import APIRequest


class UsersClient(BaseClient):
    def __init__(self, token):
        super().__init__()
        self.url = f'{self.base_url}/users'
        self.api = APIRequest()
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_users_data(self):
        return self.api.get(url=self.url, headers=self.headers)

    def get_users_meta_info(self, response):
        return response.as_dict['meta']

    def get_users_pagination_info(self, response):
        return self.get_users_meta_info(response)['pagination']

    def validate_get_users_pagination_page(self, response, expected_page=None):
        assert_value(self.get_users_pagination_info(response)['page'], expected_page)

    def validate_get_users_pagination_limit(self, response, expected_limit=None):
        assert_value(self.get_users_pagination_info(response)['limit'], expected_limit)

    def add_new_user(self, first_name=None, last_name=None, email=None, gender="Male", status="Active"):
        user_payload = get_user_payload(first_name, last_name, email, gender, status)
        return self.api.post(url=self.url, payload=user_payload, headers=self.headers)

    def added_user_data_info(self, response):
        return response.as_dict['data']

    def added_user_id(self, response):
        return self.added_user_data_info(response)["id"]

    def added_user_name(self, response):
        return self.added_user_data_info(response)["name"]

    def added_user_email(self, response):
        return self.added_user_data_info(response)["email"]

    def added_user_gender(self, response):
        return self.added_user_data_info(response)["gender"]

    def added_user_status(self, response):
        return self.added_user_data_info(response)["status"]

    def validate_attribute_value_type(self, attribute, expected_type=None):
        assert_value(type(attribute), expected_type)

    def validate_added_user_name(self, response, expected_name=None):
        assert_value(self.added_user_name(response), expected_name)

    def validate_added_user_email(self, response, expected_email=None):
        assert_value(self.added_user_email(response), expected_email)

    def validate_added_user_gender(self, response, expected_gender='Male'):
        assert_value(self.added_user_gender(response), expected_gender)

    def validate_added_user_status(self, response, expected_status='Active'):
        assert_value(self.added_user_status(response), expected_status)

    def validate_response_error_message(self, response, expected_message=None):
        assert_value(self.added_user_data_info(response)["message"], expected_message)

    def validate_error_message_for_blank(self, response, list=[]):
        assert_value(self.added_user_data_info(response)[0]["field"], list[0])
        assert_value(self.added_user_data_info(response)[0]["message"], list[1])