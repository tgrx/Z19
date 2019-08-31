from pathlib import Path

wanted_name = "User"


def wants_path(pth: Path) -> bool:
    return "lesson06" in pth.name


def wants_module(module) -> bool:
    return hasattr(module, wanted_name)


def create_user(cls, kw):
    try:
        u = cls(**kw)
        return u
    except Exception as err:
        raise AssertionError(f"failed to create {cls.__name__}(**{kw})") from err


def verify(module):
    assert hasattr(module, wanted_name), f"no `{wanted_name}` defined in {module}"

    klass = getattr(module, wanted_name)

    assert isinstance(klass, type), f"`{wanted_name}` is not a class"

    user1_args = {"name": None, "email": 1}
    user2_args = {"name": None, "email": True}
    user3_args = {"name": None, "email": False}
    user4_args = {"name": None, "email": None}

    user1 = create_user(klass, user1_args)
    user2 = create_user(klass, user2_args)
    user3 = create_user(klass, user3_args)
    user4 = create_user(klass, user4_args)

    assert hasattr(user1, "name"), f"user with {user1_args} has no `name` attr"
    assert hasattr(user2, "name"), f"user with {user2_args} has no `name` attr"
    assert hasattr(user3, "name"), f"user with {user3_args} has no `name` attr"
    assert hasattr(user4, "name"), f"user with {user4_args} has no `name` attr"

    assert hasattr(user1, "email"), f"user with {user1_args} has no `email` attr"
    assert hasattr(user2, "email"), f"user with {user2_args} has no `email` attr"
    assert hasattr(user3, "email"), f"user with {user3_args} has no `email` attr"
    assert hasattr(user4, "email"), f"user with {user4_args} has no `email` attr"

    assert user1.name == user1_args["name"]
    assert user2.name == user2_args["name"]
    assert user3.name == user3_args["name"]
    assert user4.name == user4_args["name"]

    assert user1.email == user1_args["email"]
    assert user2.email == user2_args["email"]
    assert user3.email == user3_args["email"]
    assert user4.email == user4_args["email"]

    user4.name = user4_args["name"] = "user4"
    assert user1.name == user1_args["name"]
    assert user2.name == user2_args["name"]
    assert user3.name == user3_args["name"]

    user4.email = user4_args["email"] = 0
    assert user1.email == user1_args["email"]
    assert user2.email == user2_args["email"]
    assert user3.email == user3_args["email"]

    assert user1 == user1, f"user with {user1_args} is not equal to itself"
    assert user2 == user2, f"user with {user2_args} is not equal to itself"
    assert user3 == user3, f"user with {user3_args} is not equal to itself"
    assert user4 == user4, f"user with {user4_args} is not equal to itself"

    assert user1 == user2, f"user with {user1_args} != user with {user2_args}"
    assert user2 == user1, f"user with {user2_args} != user with {user1_args}"
    assert user3 == user4, f"user with {user3_args} != user with {user4_args}"
    assert user4 == user3, f"user with {user4_args} != user with {user3_args}"

    assert not user1 == user3, f"user with {user1_args} == user with {user3_args}"
    assert not user1 == user4, f"user with {user1_args} == user with {user4_args}"

    assert not user2 == user3, f"user with {user2_args} == user with {user3_args}"
    assert not user2 == user4, f"user with {user2_args} == user with {user4_args}"

    assert not user3 == user1, f"user with {user3_args} == user with {user1_args}"
    assert not user3 == user2, f"user with {user3_args} == user with {user2_args}"

    assert not user4 == user1, f"user with {user4_args} == user with {user1_args}"
    assert not user4 == user2, f"user with {user4_args} == user with {user2_args}"

    nan = float("NaN")
    nan_args = {"name": nan, "email": nan}
    nan_user = create_user(klass, nan_args)
    assert not nan_user == nan_user, f"user with {nan_args} must be not equal to itself"

    assert not user1 == 0, f"user with {user1_args} == 0"
    assert not user1 == 1, f"user with {user1_args} == 1"
    assert not user1 == klass, f"user with {user1_args} == {klass}"
    assert not user1 == nan, f"user with {user1_args} == NaN"

    u1u1_args = {"name": None, "email": user1}
    u1u1 = create_user(klass, u1u1_args)
    assert u1u1 == u1u1, f"comparison of `User` failed: args={u1u1_args}"
