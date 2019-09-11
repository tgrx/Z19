import string


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other):
        return self.email == other.email if isinstance(other, User) else False


class UserForm(User):
    def validate_name(self):
        if not self.name:
            raise ValueError
        # a = "qwertyuiopasdfghjklzxcvbnm_"
        # b = "qwertyuiopasdfghjklzxcvbnm0123456789_"
        # c = "qwertyuiopasdfghjklzxcvbnm0123456789_."
        if self.name[0] not in (string.ascii_lowercase + '_'):
            raise ValueError
        elif self.name[-1] == '.':
            raise ValueError
        for x in self.name[1:-1]:
            if x not in (string.ascii_lowercase + string.digits + '_.'):
                raise ValueError

    def validate_email(self):
        if not self.email:
            raise ValueError
        if "@" not in self.email:
            raise ValueError
        # a = "qwertyuiopasdfghjklzxcvbnm_"
        # b = "qwertyuiopasdfghjklzxcvbnm0123456789_"
        # c = "qwertyuiopasdfghjklzxcvbnm0123456789_."
        # d = "qwertyuiopasdfghjklzxcvbnm0123456789_+."
        listemail = self.email.split("@")
        if len(listemail) != 2:
            raise ValueError
        login = listemail[0]
        domain = listemail[1]
        if not login:
            raise ValueError
        if not domain:
            raise ValueError
        if login[0] not in (string.ascii_lowercase + '_'):
            raise ValueError
        if login[-1] == '.':
            raise ValueError
        for x in login[1:-1]:
            if x not in (string.ascii_lowercase + string.digits + '_.+'):
                raise ValueError
        if domain[0] not in (string.ascii_lowercase + '_'):
            raise ValueError
        if domain[-1] == '.':
            raise ValueError
        for x in domain[1:-1]:
            if x not in (string.ascii_lowercase + string.digits + '_.'):
                raise ValueError
