class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other):
        return self.email == other.email


class UserForm(User):
    def validate_name(self):
        a = ord(self.name[0])
        b = ord(self.name[-1])
        c = ord(self.name[1:-2])
        if (not 97 <= a <= 122) and (a != 95):
            return ValueError
        if (not 97 <= b <= 122) and (not 48 <= b <= 57) and (b != 95):
            return ValueError
        if (not 97 <= c <= 122) and (not 48 <= c <= 57) and (c != 95) and (c != 46):
            return ValueError
        else:
            return self

    def validate_email(self):
        x = self.email.split('@')
        y = x[0]
        z = x[1]
        if (not 97 <= ord(y[0]), ord(z[0]) <= 122) and (ord(y[0]) != 95) and (ord(z[0]) != 95):
            return ValueError
        if (not 97 <= ord(y[-1]), ord(z[-1]) <= 122) and (not 48 <= ord(y[-1]), ord(z[-1]) <= 57) and (
                ord(y[-1]) != 95) and (ord(z[-1]) != 95):
            return ValueError
        if (not 97 <= (y[1:-2]), (z[1:-2]) <= 122) and (not 48 <= (y[1:-2]), (z[1:-2]) <= 57) and (
                (y[1:-2]) not in [95, 46, 43, ]) and ((z[1:-2]) not in [95, 46, ]):
            return ValueError
        else:
            return self
