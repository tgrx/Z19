class User:
    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"

    def __init__(self, name, email):
        if name != 0 and email != 0:
            self.name = name
            self.email = email

    def __eq__(self, other: "User"):
        return self.email == other.email


alice = User(name="alice", email="x")
bob = User(name="bob", email="x")

print(alice == bob)
