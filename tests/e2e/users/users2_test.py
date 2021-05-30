import allure
import pytest

from assertions.basic_assetions import assert_response_code
from clients.users.users_client import UsersClient
from util.generic_helper import generate_random_string, generate_random_email_address


@allure.step
@pytest.fixture(scope='class')
def init_test():
    invalid_token = '687ccbe4e07bf7e4cd20e210a8ec9711c3039ad1db87765c48b3a419bf8d64ac00'
    user = UsersClient(invalid_token)
    return user


@allure.step
@pytest.mark.negative
def test_user_add_when_invalid_token_passed(init_test):
    # getting returned value from fixture
    user = init_test

    # generated random values, based on these values we are forming the payload on clients >> users >> user_payload.py
    user_first_name = generate_random_string(8, "autof")
    user_last_name = generate_random_string(8, "autol")
    user_email = generate_random_email_address(8, "auto")

    # getting response object value
    json_response = user.add_new_user(first_name=user_first_name, last_name=user_last_name, email=user_email)

    # validate response status code
    assert_response_code(json_response, 401)

    # validate error message from response
    user.validate_response_error_message(json_response, "Authentication failed")