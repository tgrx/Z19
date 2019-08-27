from pathlib import Path
from typing import Callable

wanted_name = "Range"


def wants_path(pth: Path) -> bool:
    return "lesson05" in pth.name


def wants_module(module) -> bool:
    return hasattr(module, wanted_name)


def verify(module):
    assert hasattr(module, wanted_name), f"no `{wanted_name}` defined in {module}"

    r = getattr(module, wanted_name)

    assert isinstance(r, Callable), f"`{wanted_name}` is not callable"

    dataset = (
        (0,),
        (10,),
        (0, 10,),
        (10, 0,),
        (1, 10,),
        (10, 1,),
        (0, 10, -2),
        (0, 10, 2),
        (0, -10, -2),
        (0, -10, 2),
    )

    for args in dataset:
        assert tuple(r(*args)) == tuple(range(*args))

    assert 2 in r(10, -10, -1)

    assert not isinstance(r(1), (list, tuple, str))
