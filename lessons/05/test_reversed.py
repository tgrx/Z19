from pathlib import Path
from typing import Callable


def wants_path(pth: Path) -> bool:
    return "lesson05" in pth.name


def wants_module(module) -> bool:
    return True


def verify(module):
    name = "reversed2"

    assert hasattr(module, name), f"no `{name}` defined in {module}"

    reversed2 = getattr(module, "reversed2")

    assert isinstance(reversed2, Callable), f"`{name}` is not callable"

    assert reversed2([]) == []
    assert reversed2([3, 2, 1]) == [1, 2, 3]
    assert reversed2([1, 1, 1]) == [1, 1, 1]
