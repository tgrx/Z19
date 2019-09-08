class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other):
        return self.email == other.email


class UserForm(User):
    def validate_name(self):
        if self.name[0] not in 'qwertyuiopasdfghjklzxcvbnm_':
            return ValueError
        if self.name[-1] not in 'qwertyuiopasdfghjklzxcvbnm0123456789_':
            return ValueError
        slice = self.name[1:-2]
        for x in slice:
            if x not in 'qwertyuiopasdfghjklzxcvbnm0123456789_.':
                return ValueError
        else:
            return self

    def validate_email(self):
        lisemail = self.email.split("@")
        login = lisemail[0]
        domain = lisemail[1]
        if login[0] not in 'qwertyuiopasdfghjklzxcvbnm_':
            return ValueError
        if login[-1] not in 'qwertyuiopasdfghjklzxcvbnm_0123456789':
            return ValueError
        slice = self.name[1:-2]
        for x in slice:
            if x not in 'qwertyuiopasdfghjklzxcvbnm0123456789_+.':
                return ValueError
        if domain[0] not in 'qwertyuiopasdfghjklzxcvbnm_.':
            return ValueError
        if domain[-1] not in 'qwertyuiopasdfghjklzxcvbnm0123456789_':
            return ValueError
        slice = self.name[1:-2]
        for x in slice:
            if x not in 'qwertyuiopasdfghjklzxcvbnm0123456789_.':
                return ValueError
        else:
            return self
