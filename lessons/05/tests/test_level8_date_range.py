import ast
from pathlib import Path
from typing import Callable

wanted_name = "DateRange"


def verify_no_prohibited_calls(module_path):
    prohibited_names = {"print"}

    with open(module_path, "r") as module:
        code = module.read()

        tree = ast.parse(code)

        for node in ast.walk(tree):
            if not isinstance(node, ast.Name):
                continue

            assert node.id not in prohibited_names, (
                f"`{node.id}` detected in {module_path}"
                f" at {node.lineno}:{node.col_offset}"
                f" - must not use"
            )


def wants_path(pth: Path) -> bool:
    return "lesson05" in pth.name


def wants_module(module) -> bool:
    return hasattr(module, wanted_name)


def verify(module):
    verify_no_prohibited_calls(module.__file__)

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
