from pathlib import Path
from typing import Callable

wanted_name = "compare_triplets"


def wants_path(pth: Path) -> bool:
    return "lesson17" in pth.name


def wants_module(_module):
    return True


def verify(module):
    assert hasattr(module, wanted_name), f"no `{wanted_name}` defined in {module}"

    f = getattr(module, wanted_name)

    assert isinstance(f, Callable), f"`{wanted_name}` is not callable"

    checks = {
        ((0, 0, 0), (1, 1, 1)): (0, 3),
        ((1, 1, 0), (0, 1, 0)): (1, 0),
        ((1, 1, 1), (0, 0, 0)): (3, 0),
        ((1, 1, 1), (1, 1, 1)): (0, 0),
        ((10, 20, 30), (20, 30, 10)): (1, 2),
    }

    for origin, expected in checks.items():
        got = f(*origin)
        assert (
            got == expected
        ), f"{wanted_name}({origin!r}) != {expected!r}: returned {got!r}"
