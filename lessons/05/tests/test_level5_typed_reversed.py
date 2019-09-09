import ast
from pathlib import Path
from typing import Callable

wanted_name = "TypedReversed"


def verify_no_prohibited_calls(module_path):
    # prohibited_names = {"print", "reversed", "range"}
    prohibited_names = {"print"}

    with open(module_path, "r") as module:
        code = module.read()

        tree = ast.parse(code)

        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Subscript)
                and isinstance(node.slice, ast.Slice)
                and node.slice.lower is None
                and node.slice.upper is None
                and node.slice.step is not None
                and isinstance(node.slice.step.op, ast.USub)
                and isinstance(node.slice.step.operand, ast.Num)
                and node.slice.step.operand.n == 1
            ):
                raise AssertionError(
                    f"reversing slice [::-1] detected in {module_path}"
                    f" at {node.lineno}:{node.col_offset}"
                    f" - must not use"
                )

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

    assert r([]) == []
    assert r([3, 2, 1]) == [1, 2, 3]
    assert r([1, 1, 1]) == [1, 1, 1]
    assert r([]) == []
    assert r((3, 2, 1)) == (1, 2, 3)
    assert r("aacb") == "bcaa"
