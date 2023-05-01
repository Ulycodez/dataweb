import pytest
#  (1, 1, 'johndoe', 'password123'),
#    (1, 1, 1, 'John', 'Doe'),
#id website_id first name, last name username, password

@pytest.fixture
def input_value():
    input = "John", "Doe", "johndoe", "password123",
    return input

def new_user():
    firstname = "John"
    lastname = "Doe"
    username = "johndoe"
    password = "password123"
    return firstname, lastname, username, password


def test_new_user(input_value):
    assert new_user() == input_value
