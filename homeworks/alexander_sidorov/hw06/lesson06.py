import string


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other):
        if not isinstance(other, User):
            return False

        return self.email == other.email


class UserForm(User):
    def validate_name(self):
        if not self.name:
            raise ValueError

        if self.name[0] in (string.digits + "."):
            raise ValueError

        if self.name[-1] == ".":
            raise ValueError

        valid_chars = string.ascii_lowercase + string.digits + "." + "_"

        for c in self.name:
            if c not in valid_chars:
                raise ValueError

    def validate_email(self):
        if not self.email:
            raise ValueError

        if "@" not in self.email:
            raise ValueError

        login, domain = self.email.split("@")

        # validate login

        if not login:
            raise ValueError

        if login[0] in (string.digits + ".+"):
            raise ValueError

        if login[-1] in ".+":
            raise ValueError

        valid_chars = string.ascii_lowercase + string.digits + "._+"

        for c in login:
            if c not in valid_chars:
                raise ValueError

        # validate domain

        if not domain:
            raise ValueError

        if domain[0] in (string.digits + "."):
            raise ValueError

        if domain[-1] == ".":
            raise ValueError

        valid_chars = string.ascii_lowercase + string.digits + "._"

        for c in domain:
            if c not in valid_chars:
                raise ValueError
