from pathlib import Path
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

    checks = {"": "", "a": "a1", "ab": "a1b1", "aaaaabbbc": "a5b3c1"}

    for origin, expected in checks.items():
        got = f(origin)
        assert (
            got == expected
        ), f"{wanted_name}({origin!r}) != {expected!r}: returned {got!r}"
