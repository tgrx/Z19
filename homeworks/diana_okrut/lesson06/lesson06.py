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
        a = "qwertyuiopasdfghjklzxcvbnm_"
        b = "qwertyuiopasdfghjklzxcvbnm0123456789_"
        c = "qwertyuiopasdfghjklzxcvbnm0123456789_."
        if self.name[0] not in a:
            raise ValueError
        elif self.name[-1] not in b:
            raise ValueError
        for x in self.name[1:-1]:
            if x not in c:
                raise ValueError

    def validate_email(self):
        if not self.email:
            raise ValueError
        if '@' not in self.email:
            raise ValueError
        a = "qwertyuiopasdfghjklzxcvbnm_"
        b = "qwertyuiopasdfghjklzxcvbnm0123456789_"
        c = "qwertyuiopasdfghjklzxcvbnm0123456789_."
        d = "qwertyuiopasdfghjklzxcvbnm0123456789_+."
        lisemail = self.email.split("@")
        login = lisemail[0]
        domain = lisemail[1]
        if login[0] not in a:
            raise ValueError
        if login[-1] not in b:
            raise ValueError
        for x in login[1: -1]:
            if x not in d:
                raise ValueError
        if domain[0] not in a:
            raise ValueError
        if domain[-1] not in b:
            raise ValueError
        for x in domain[1: -1]:
            if x not in c:
                raise ValueError
