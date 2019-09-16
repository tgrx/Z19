class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, email={self.email!r})"


#   def compare():


alice = User(name="alice", email="x")
bob = User(name="bob", email="x")

print(alice)
print(bob)
print(alice == bob)
