class User:
    def __repr__(self):
        return f"User(name = {self.name}, email = {self.email})"

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other: "User"):
        return self.email == other.email


user1 = User("1", "@")
user2 = User("1", "@")
print(user1 == user2)
