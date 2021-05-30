import pytest


@pytest.fixture(scope="session", autouse=True)
def before_test():
    print("Test case started....")
    yield
    print("Test case completed....")