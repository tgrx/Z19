from pathlib import Path
from typing import Callable

wanted_name = "DateRange"


def wants_path(pth: Path) -> bool:
    return "lesson05" in pth.name


def wants_module(module) -> bool:
    return hasattr(module, wanted_name)


def verify(module):
    assert hasattr(module, wanted_name), f"no `{wanted_name}` defined in {module}"

    r = getattr(module, wanted_name)

    assert isinstance(r, Callable), f"`{wanted_name}` is not callable"

    from datetime import date as d, timedelta as t

    today = d.today()
    tomorrow = today + t(days=1)
    next_week = today + t(days=7)

    assert tomorrow in r(today, next_week)

    assert tuple(r(tomorrow, next_week)) == (
        today,
        today + t(days=1),
        today + t(days=2),
        today + t(days=3),
        today + t(days=4),
        today + t(days=5),
        today + t(days=6),
    )
