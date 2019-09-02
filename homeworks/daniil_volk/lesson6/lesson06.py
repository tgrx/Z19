class User:
    def __init__(self, name, emeil):
        self.name = name
        self.emeil = emeil

    def __eq__(self, other):
        if type(self) == type(other):
            return self.emeil == other.emeil
        else:
            raise TypeError


class UserForm(User):
    def validate_name(self):
        if isinstance(self.name[0], int):
            return ValueError
        if self.name[0] == '.' or self.name[-1] == '.':
            return ValueError
        a = (not any(c.islower() for c in self.name))
        b = (not self.name.isnumeric())
        c = (self.name != '_')
        d = (not '.' in self.name)
        if a and b and c and d:
            return ValueError

    def validate_email(self):
        em = self.emeil.split("@")
        log = em[0]
        dom = em[1]

        if log[0] == '+' or log[-1] == '+'
            return ValueError
        if isinstance(log[0], int):
            return ValueError
        if log[0] == '.' or log[-1] == '.':
            return ValueError
        a = (not any(c.islower() for c in log))
        b = (not log.isnumeric())
        c = (log != '_')
        d = (not '.' in log)
        e = (not '+' in log)
        if a and b and c and d and e:
            return ValueError