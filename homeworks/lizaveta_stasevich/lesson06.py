import re


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other):
        if self.email == other.email:
            return True


class UserForm:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def validate_name(self):
        if self.name[0].isdigit() and self.name[0] != ".":
            if self.name[-1] != ".":
                pass
        else:
            raise ValueError


alice = UserForm(name="455ggп2", email="x")
alice.validate_name()

