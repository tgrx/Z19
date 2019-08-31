class User:
    def __repr__(self):
        return f"User(name=`{self.name}`, email=`{self.email}`)"

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __eq__(self, other: "User"):
        if not isinstance(other, User):
            return False
        return self.email == other.email and self.name == other.name


u1 = User("a", "@")
u2 = User("b", "@")

print(u1)
print(u2)


def main():
    print(u1 == u1)


main()
