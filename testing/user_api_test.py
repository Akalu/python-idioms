import pytest

from testing.user_api import UserController
from testing.user_schema import UserSchema


@pytest.fixture
def min_user():
    """Represent a valid user with minimal data. """
    return {
        'email': 'jsmith@mail.com',
        'name': 'John Smith',
        'age': 18,
    }


@pytest.fixture
def full_user():
    """Represent valid user with full data. """
    return {
        'email': 'alice@mail.com',
        'name': 'Alice Atwood',
        'age': 65,
        'role': 'writer',
    }


@pytest.fixture
def users(min_user, full_user):
    """List of users, two valid and one invalid. """
    bad_user = {
        'email': 'invalid@mail.com',
        'name': 'Unknown',
    }
    return [min_user, bad_user, full_user]


class TestIsValid:
    """Test how code verifies whether a user is valid or not. """

    schema = UserSchema()
    controller = UserController(schema)

    def test_minimal(self, min_user):
        assert self.controller.is_valid(min_user)

    def test_full(self, full_user):
        assert self.controller.is_valid(full_user)
