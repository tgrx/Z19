class User:
    def __repr__(self):
        return f"User(name=`{self.name}`, email=`{self.email}`)"

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other): 
        if not isinstance(other, User):
            return NotImplemented

        return self.name == other.name or self.email == other.email


user1 = User('abc', 'peter')
print(user1)

user2 = User('bca', 'peter')
print(user2)

r = user1 == user2
print(r)
