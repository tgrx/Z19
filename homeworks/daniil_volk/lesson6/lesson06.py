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
        n = self.name
        if not n:
            raise ValueError
        if (
            not (any(c.islower() for c in n))
            and not (any(c.isdigit() for c in n))
            and not n == "_"
            or not (any(c.isalpha() for c in n))
            and not (any(c.isdigit() for c in n))
            and not n == "_"
            or n[0] == "."
            or n[(len(n) - 1)] == "."
            or n[0] == "+"
            or n[(len(n) - 1)] == "+"
            or n[0] == "@"
            or n[(len(n) - 1)] == "@"
            or n[0] == "-"
            or n[(len(n) - 1)] == "-"
            or n[0].isnumeric()
        ):
            raise ValueError

    def validate_email(self):
        if not self.email:
            raise ValueError
        if not "@" in self.email:
            raise ValueError
        em = self.email.split("@")
        if not em[0] or not em[1]:
            raise ValueError
        log = em[0]
        dom = em[1]
        if not log:
            raise ValueError
        if not dom:
            raise ValueError

        if (
            not (any(c.islower() for c in log))
            and not (any(c.isdigit() for c in log))
            and not log == "_"
            or not (any(c.isalpha() for c in log))
            and not (any(c.isdigit() for c in log))
            and not log == "_"
            or log[0] == "."
            or log[(len(log) - 1)] == "."
            or log[0] == "+"
            or log[(len(log) - 1)] == "+"
            or log[0] == "@"
            or log[(len(log) - 1)] == "@"
            or log[0] == "-"
            or log[(len(log) - 1)] == "-"
            or log[0].isnumeric()
        ):
            raise ValueError

        if (
            not (any(c.islower() for c in dom))
            and not (any(c.isdigit() for c in dom))
            and not dom == "_"
            or not (any(c.isalpha() for c in dom))
            and not (any(c.isdigit() for c in dom))
            and not dom == "_"
            or dom[0] == "."
            or dom[(len(dom) - 1)] == "."
            or dom[0] == "+"
            or dom[(len(dom) - 1)] == "+"
            or dom[0] == "@"
            or dom[(len(dom) - 1)] == "@"
            or dom[0] == "-"
            or dom[(len(dom) - 1)] == "-"
            or dom[0].isnumeric()
        ):
            raise ValueError
