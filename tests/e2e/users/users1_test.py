import allure
import pytest

from assertions.basic_assetions import assert_response_code, assert_value
from clients.users.delete_user_client import DeleteUserClient
from clients.users.users_client import UsersClient
from util.generic_helper import generate_random_string, generate_random_email_address

valid_token = '687ccbe4e07bf7e4cd20e210a8ec9711c3039ad1db87765c48b3a419bf8d64ac'


@allure.step
@pytest.fixture(scope='class')
def init_test():
    user = UsersClient(valid_token)
    return user


@allure.step
@pytest.mark.positive
def test_get_users_list(init_test):
    # getting returned value from fixture
    user = init_test

    # getting response object value
    json_response = user.get_users_data()

    # validate response status code
    assert_response_code(json_response, 200)

    # validate page value and pagination limit value
    user.validate_get_users_pagination_page(json_response, 1)
    user.validate_get_users_pagination_limit(json_response, 20)


@allure.step
@pytest.mark.positive
def test_user_added_when_valid_token_passed(init_test):
    # getting returned value from fixture
    user = init_test

    # generated random values, based on these values we are forming the payload on clients >> users >> user_payload.py
    user_first_name = generate_random_string(8, "autof")
    user_last_name = generate_random_string(8, "autol")
    user_email = generate_random_email_address(8, "auto")

    # getting response object value
    json_response = user.add_new_user(first_name=user_first_name, last_name=user_last_name, email=user_email)

    # validate response status code
    assert_response_code(json_response, 201)

    # user full name
    full_name = user_first_name + " " + user_last_name

    # validate created user full name
    user.validate_added_user_name(json_response, full_name)

    # validate created user email
    user.validate_added_user_email(json_response, user_email)

    # validate created user status and gender (put static here can be passed as argument as well to form dynamic payload
    user.validate_added_user_gender(json_response, "Male")
    user.validate_added_user_status(json_response, "Active")

    # validate created user id is int
    user.validate_attribute_value_type(user.added_user_id(json_response), int)


@allure.step
@pytest.mark.negative
def test_user_add_when_blank_email_in_payload(init_test):
    # getting returned value from fixture
    user = init_test

    # generated random values, based on these values we are forming the payload on clients >> users >> user_payload.py
    user_first_name = generate_random_string(8, "autof")
    user_last_name = generate_random_string(8, "autol")
    user_email = ''

    # getting response object value
    json_response = user.add_new_user(first_name=user_first_name, last_name=user_last_name, email=user_email)

    # validate response status code
    assert_response_code(json_response, 422)

    # validate created user id is int
    user.validate_error_message_for_blank(json_response, ["email", "can't be blank"])


@allure.step
@pytest.mark.negative
def test_user_add_when_blank_name_in_payload(init_test):
    # getting returned value from fixture
    user = init_test

    # generated random values, based on these values we are forming the payload on clients >> users >> user_payload.py
    user_first_name = ''
    user_last_name = ''
    user_email = generate_random_email_address(8, "auto")

    # getting response object value
    json_response = user.add_new_user(first_name=user_first_name, last_name=user_last_name, email=user_email)

    # validate response status code
    assert_response_code(json_response, 422)

    # validate created user id is int
    user.validate_error_message_for_blank(json_response, ["name", "can't be blank"])


@allure.step
@pytest.mark.negative
def test_user_add_when_long_name_in_payload(init_test):
    # getting returned value from fixture
    user = init_test

    # generated random values, based on these values we are forming the payload on clients >> users >> user_payload.py
    user_first_name = generate_random_string(100, "autof")
    user_last_name = generate_random_string(100, "autol")
    user_email = generate_random_email_address(8, "auto")
    # getting response object value
    json_response = user.add_new_user(first_name=user_first_name, last_name=user_last_name, email=user_email)

    # validate response status code
    assert_response_code(json_response, 422)

    # validate created user id is int
    user.validate_error_message_for_blank(json_response, ["name", "is too long (maximum is 200 characters)"])


@allure.step
@pytest.mark.negative
def test_user_add_when_blank_gender_in_payload(init_test):
    # getting returned value from fixture
    user = init_test

    # generated random values, based on these values we are forming the payload on clients >> users >> user_payload.py
    user_first_name = generate_random_string(8, "autof")
    user_last_name = generate_random_string(8, "autol")
    user_email = generate_random_email_address(8, "auto")
    gender = ''
    # getting response object value
    json_response = user.add_new_user(first_name=user_first_name, last_name=user_last_name, email=user_email,
                                      gender=gender)

    # validate response status code
    assert_response_code(json_response, 422)

    # validate created user id is int
    user.validate_error_message_for_blank(json_response, ["gender", "can't be blank"])


@allure.step
@pytest.mark.negative
def test_user_add_when_blank_status_in_payload(init_test):
    # getting returned value from fixture
    user = init_test

    # generated random values, based on these values we are forming the payload on clients >> users >> user_payload.py
    user_first_name = generate_random_string(8, "autof")
    user_last_name = generate_random_string(8, "autol")
    user_email = generate_random_email_address(8, "auto")
    status = ''
    # getting response object value
    json_response = user.add_new_user(first_name=user_first_name, last_name=user_last_name, email=user_email,
                                      status=status)

    # validate response status code
    assert_response_code(json_response, 422)

    # validate created user id is int
    user.validate_error_message_for_blank(json_response, ["status", "can't be blank"])


@allure.step
@pytest.mark.negative
def test_user_add_when_invalid_status_in_payload(init_test):
    # getting returned value from fixture
    user = init_test

    # generated random values, based on these values we are forming the payload on clients >> users >> user_payload.py
    user_first_name = generate_random_string(8, "autof")
    user_last_name = generate_random_string(8, "autol")
    user_email = generate_random_email_address(8, "auto")
    status = 'Blacklist'
    # getting response object value
    json_response = user.add_new_user(first_name=user_first_name, last_name=user_last_name, email=user_email,
                                      status=status)

    # validate response status code
    assert_response_code(json_response, 422)

    # validate created user id is int
    user.validate_error_message_for_blank(json_response, ["status", "can be Active or Inactive"])


@allure.step
@pytest.mark.negative
def test_user_add_when_invalid_gender_in_payload(init_test):
    # getting returned value from fixture
    user = init_test

    # generated random values, based on these values we are forming the payload on clients >> users >> user_payload.py
    user_first_name = generate_random_string(8, "autof")
    user_last_name = generate_random_string(8, "autol")
    user_email = generate_random_email_address(8, "auto")
    gender = 'Kid'
    # getting response object value
    json_response = user.add_new_user(first_name=user_first_name, last_name=user_last_name, email=user_email,
                                      gender=gender)

    # validate response status code
    assert_response_code(json_response, 422)

    # validate created user id is int
    user.validate_error_message_for_blank(json_response, ["gender", "can be Male or Female"])


@allure.step
@pytest.mark.positive
def test_delete_added_user(init_test):
    # getting returned value from fixture
    user = init_test
    # generated random values, based on these values we are forming the payload on clients >> users >> user_payload.py
    user_first_name = generate_random_string(8, "autof")
    user_last_name = generate_random_string(8, "autol")
    user_email = generate_random_email_address(8, "auto")
    # getting response object value
    json_response = user.add_new_user(first_name=user_first_name, last_name=user_last_name, email=user_email)
    # validate response status code
    assert_response_code(json_response, 201)
    # validate created user id is int
    user_delete = DeleteUserClient(valid_token, user.added_user_id(json_response))
    json_response = user_delete.delete_user()
    assert_response_code(json_response, 204)
    assert_value(json_response.as_dict['data'], None)


@allure.step
@pytest.mark.negative
def test_delete_invalid_user(init_test):
    # getting returned value from fixture
    user = init_test
    # generated random values, based on these values we are forming the payload on clients >> users >> user_payload.py
    user_first_name = generate_random_string(8, "autof")
    user_last_name = generate_random_string(8, "autol")
    user_email = generate_random_email_address(8, "auto")
    # getting response object value
    json_response = user.add_new_user(first_name=user_first_name, last_name=user_last_name, email=user_email)
    # validate response status code
    assert_response_code(json_response, 201)
    # trying to delete a user which not exists
    user_id = user.added_user_id(json_response) + 1
    user_delete = DeleteUserClient(valid_token, user_id)
    json_response = user_delete.delete_user()
    assert_response_code(json_response, 404)
    assert_value(json_response.as_dict['data']['message'], 'Resource not found')