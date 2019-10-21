import string
from pathlib import Path
from random import choice
from typing import Callable

wanted_name = "Zip"


def wants_path(pth: Path) -> bool:
    return "lesson16" in pth.name


def wants_module(_module):
    return True


def verify(module):
    assert hasattr(module, wanted_name), f"no `{wanted_name}` defined in {module}"

    f = getattr(module, wanted_name)

    assert isinstance(f, Callable), f"`{wanted_name}` is not callable"

    a, b, c, d = [choice(string.ascii_letters) for _ in "1234"]

    checks = {
        "": "",
        f"{a * 5}{b * 3}{c}{d}": f"{a}5{b}3{c}1{d}1",
        f"{a * 13}{b * 13}{c}{d * 13}": f"{a}13{b}13{c}1{d}13",
        f"{a}": f"{a}1",
        f"{a}{b}": f"{a}1{b}1",
    }

    for origin, expected in checks.items():
        got = f(origin)
        assert (
            got == expected
        ), f"{wanted_name}({origin!r}) != {expected!r}: returned {got!r}"
