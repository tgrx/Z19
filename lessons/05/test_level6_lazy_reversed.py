from pathlib import Path
from typing import Callable

wanted_name = "LazyReversed"


def wants_path(pth: Path) -> bool:
    return "lesson05" in pth.name


def wants_module(module) -> bool:
    return hasattr(module, wanted_name)


def verify(module):
    assert hasattr(module, wanted_name), f"no `{wanted_name}` defined in {module}"

    r = getattr(module, wanted_name)

    assert isinstance(r, Callable), f"`{wanted_name}` is not callable"

    assert not isinstance(r([]), (list, tuple, str))
    assert not isinstance(r(()), (list, tuple, str))
    assert not isinstance(r(""), (list, tuple, str))
    assert list(r([])) == []
    assert tuple(r([3, 2, 1])) == (1, 2, 3)
