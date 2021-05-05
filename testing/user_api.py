import csv
import os

from testing.user_schema import UserSchema


class UserController(UserSchema):
    """Represents an interface to functionality to work with users
    """

    def __init__(self, schema):
        self.schema = schema

    def export(self, filename, users, overwrite=True):
        """Export a CSV file.

        Create a CSV file and fill with valid users. If `overwrite`
        is False and file already exists, raise IOError.
        """
        if not overwrite and os.path.isfile(filename):
            raise IOError(f"'{filename}' already exists.")

        valid_users = self.get_valid_users(users)
        self.write_csv(filename, valid_users)

    def get_valid_users(self, users):
        """Yield one valid user at a time from users. """
        yield from filter(self.is_valid, users)

    def is_valid(self, user):
        """Return whether or not the user is valid. """
        return not self.schema.validate(user)

    @staticmethod
    def write_csv(self, filename, users):
        """Write a CSV given a filename and a list of users.

        The users are assumed to be valid for the given CSV structure.
        """
        fieldnames = ['email', 'name', 'age', 'role']

        with open(filename, 'x', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for user in users:
                writer.writerow(user)
