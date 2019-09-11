class User:
    def __init__(self, n, e):     # initialize
        self.name = n
        self.email = e

    def f(self):
        return f"name={self.name}, email={self.email}"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        r = (self.email == other.email)
        return r
