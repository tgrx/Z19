import ast
from pathlib import Path
from typing import Callable

wanted_name = "Sorted"


def verify_no_prohibited_calls(module_path):
    # prohibited_names = {"print", "sorted"}
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

    assert r([]) == [], f"Sorted([]) => `{r([])}`, while expected: []"
    assert r((3, 1, 2)) == [
        1,
        2,
        3,
    ], f"Sorted((3,1,2)) => `{r((3, 1, 2))}`, while expected: [1, 2, 3]"
    assert r("zxy") == [
        "x",
        "y",
        "z",
    ], f'Sorted("zxy") => `{r("zxy")}`, while expected: ["x", "y", "z"]'
    assert r({3, 1, 1, 2}) == [
        1,
        2,
        3,
    ], f"Sorted({3, 1, 1, 2}) => `{r({3, 1, 1, 2})}`, while expected: [1, 2, 3]"
