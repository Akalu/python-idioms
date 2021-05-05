import pytest

from testing.user_api import UserController
from testing.user_schema import UserSchema


# this section defines the base structures (records, maps, etc) which will be used in tests
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


# base class containing all unit-tests
class TestIsValid:
    """Test how code verifies whether a user is valid or not. """

    # first instantiate all types we are going to test
    schema = UserSchema()
    controller = UserController(schema)

    # unit tests themselves
    # Note: we are heavily using parameterization
    def test_minimal(self, min_user):
        assert self.controller.is_valid(min_user)

    def test_full(self, full_user):
        assert self.controller.is_valid(full_user)

    # define parameters to test against
    @pytest.mark.parametrize('age', range(66, 100))
    def test_invalid_age_too_old(self, age, min_user):
        min_user['age'] = age
        assert not self.controller.is_valid(min_user)

    @pytest.mark.parametrize('age', ['NaN', 3.1415, None])
    def test_invalid_age_wrong_type(self, age, min_user):
        min_user['age'] = age
        assert not self.controller.is_valid(min_user)

    @pytest.mark.parametrize('age', range(18, 66))
    def test_valid_age(self, age, min_user):
        min_user['age'] = age
        assert self.controller.is_valid(min_user)

    @pytest.mark.parametrize('field', ['email', 'name', 'age'])
    def test_mandatory_fields(self, field, min_user):
        min_user.pop(field)
        assert not self.controller.is_valid(min_user)

    @pytest.mark.parametrize('field', ['email', 'name', 'age'])
    def test_mandatory_fields_empty(self, field, min_user):
        min_user[field] = ''
        assert not self.controller.is_valid(min_user)

    def test_name_whitespace_only(self, min_user):
        min_user['name'] = ' \n\t'
        assert not self.controller.is_valid(min_user)

    # define tuples (email, outcome) to test against
    @pytest.mark.parametrize(
        'email, outcome',
        [
            ('missing_at.com', False),
            ('@missing_start.com', False),
            ('missing_end@', False),
            ('missing_dot@example', False),

            ('good.one@example.com', True),
            ('test.test@mail.com', True),
        ]
    )
    def test_email(self, email, outcome, min_user):
        min_user['email'] = email
        assert self.controller.is_valid(min_user) == outcome
