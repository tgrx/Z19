class User:
    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other: "User"):
        return self.email == other.email

    u1 = User("1", "@")
    u2 = User("1", "@")
    print(u1 == u2)
