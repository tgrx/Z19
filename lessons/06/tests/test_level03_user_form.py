from pathlib import Path
from typing import Callable

wanted_name = "UserForm"


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
    assert hasattr(module, "User"), f"no `User` defined in {module}"

    k_form = getattr(module, wanted_name)
    k_obj = getattr(module, "User")

    assert isinstance(k_form, type), f"`{wanted_name}` is not a class"
    assert isinstance(k_obj, type), f"`User` is not a class"
    assert issubclass(k_form, k_obj), f"{wanted_name} is not a subclass of User"

    meth_vn_name = "validate_name"
    assert hasattr(k_form, meth_vn_name), f"{wanted_name} has no attr {meth_vn_name}"
    meth_vn = getattr(k_form, meth_vn_name)
    assert isinstance(
        meth_vn, Callable
    ), f"{wanted_name}.{meth_vn_name} is not callable"

    meth_ve_name = "validate_email"
    assert hasattr(k_form, meth_ve_name), f"{wanted_name} has no attr {meth_ve_name}"
    meth_ve = getattr(k_form, meth_ve_name)
    assert isinstance(
        meth_ve, Callable
    ), f"{wanted_name}.{meth_ve_name} is not callable"

    valid_names = {
        "_",
        "_1",
        "_a",
        "_a.1",
        "_a.1_",
        "_a_",
        "a",
        "a.1",
        "a.1_",
        "a._1",
        "a1",
        "a_",
        "a_.1",
        "a_1",
    }

    invalid_names = {
        "",
        "+1",
        "+a",
        "-1",
        "-a",
        "1",
        "1+",
        "1-",
        "1_",
        "1a",
        "@a",
        "a+",
        "a-",
        "a@",
    }

    valid_logins = {
        "_",
        "_1",
        "_a",
        "_a+.1",
        "_a+1",
        "_a.+.1",
        "_a.+1",
        "_a.1",
        "_a.1_",
        "_a_",
        "a",
        "a+a",
        "a+a",
        "a.1",
        "a.1_",
        "a._1",
        "a1",
        "a_",
        "a_.1",
        "a_1",
    }

    invalid_logins = {
        "",
        "+1",
        "+a",
        "-1",
        "-a",
        ".1",
        ".1.",
        ".a",
        ".a.",
        "1",
        "1+",
        "1-",
        "1.",
        "1_",
        "1a",
        "@a",
        "a+",
        "a+.",
        "a-",
        "a.",
        "a.+",
        "a@",
    }

    valid_emails = {
        p + _n for p in {"{}@".format(_l) for _l in valid_logins} for _n in valid_names
    } | {"alex.n.sidorov+z19@gmail.com"}

    invalid_emails = (
        {
            p + _n
            for p in {"{}@".format(_l) for _l in invalid_logins}
            for _n in valid_names
        }
        | {
            p + _n
            for p in {"{}@".format(_l) for _l in valid_logins}
            for _n in invalid_names
        }
        | {
            p + _n
            for p in {"{}@".format(_l) for _l in invalid_logins}
            for _n in invalid_names
        }
    )

    for n in valid_names:
        a = {"name": n, "email": None}
        f = create_user(k_form, a)
        try:
            f.validate_name()
        except ValueError as err:
            raise AssertionError(
                f"valid name {n!r} treated as invalid for {a}"
            ) from err
        except Exception as err:
            raise AssertionError(
                f"validator {k_form}.{meth_vn_name} raises {err} for valid name {n!r}"
            ) from err

    for n in invalid_names:
        a = {"name": n, "email": None}
        f = create_user(k_form, a)
        try:
            f.validate_name()
        except ValueError:
            pass
        except Exception as err:
            raise AssertionError(
                f"validator {k_form}.{meth_vn_name} raises {err} for invalid name {n!r}"
            ) from err
        else:
            raise AssertionError(f"invalid name {n!r} treated as valid for {a}")

    for n in valid_emails:
        a = {"name": None, "email": n}
        f = create_user(k_form, a)
        try:
            f.validate_email()
        except ValueError as err:
            raise AssertionError(
                f"valid email {n!r} treated as invalid for {a}"
            ) from err
        except Exception as err:
            raise AssertionError(
                f"validator {k_form}.{meth_vn_name} raises {err} for valid email {n!r}"
            ) from err

    for n in invalid_names:
        a = {"name": None, "email": n}
        f = create_user(k_form, a)
        try:
            f.validate_email()
        except ValueError:
            pass
        except Exception as err:
            raise AssertionError(
                f"validator {k_form}.{meth_vn_name} raises {err} for invalid email {n!r}"
            ) from err
        else:
            raise AssertionError(f"invalid email {n!r} treated as valid for {a}")
