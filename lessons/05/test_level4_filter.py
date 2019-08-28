from pathlib import Path
from typing import Callable

wanted_name = "Filter"


def wants_path(pth: Path) -> bool:
    return "lesson05" in pth.name


def wants_module(module) -> bool:
    return hasattr(module, wanted_name)


def verify(module):
    assert hasattr(module, wanted_name), f"no `{wanted_name}` defined in {module}"

    r = getattr(module, wanted_name)

    assert isinstance(r, Callable), f"`{wanted_name}` is not callable"

    assert r(bool, [0, 1, 2]) == [1, 2]
    assert r(bool, []) == []

    def kek(s):
        return "kek" in s

    assert r(kek, ["ke", "kek", "keke", "ekek", "lul"]) == ["kek", "keke", "ekek"]
