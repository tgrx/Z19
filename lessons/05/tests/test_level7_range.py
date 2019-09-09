import ast
from pathlib import Path
from typing import Callable

wanted_name = "Range"


def verify_no_prohibited_calls(module_path):
    # prohibited_names = {"print", "range"}
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

    dataset = (
        (0,),
        (10,),
        (0, 10),
        (10, 0),
        (1, 10),
        (10, 1),
        (0, 10, -2),
        (0, 10, 2),
        (0, -10, -2),
        (0, -10, 2),
    )

    for args in dataset:
        x = tuple(r(*args))
        assert tuple(r(*args)) == tuple(
            range(*args)
        ), f"failed on {wanted_name}{args}: {x}"

    assert 2 in r(10, -10, -1)

    assert not isinstance(r(1), (list, tuple, str))
