from assertpy import assert_that


def assert_response_code(response, expected):
    actual = response.as_dict['code']
    print("Going to check response status code:: expected response code: {} and actual response code: {}".format(expected, actual))
    assert_that(actual).is_equal_to(int(expected))


def assert_value(actual, expected):
    print("Going to check response values:: expected value: {} and actual value: {}".format(expected, actual))
    assert_that(actual).is_equal_to(expected)