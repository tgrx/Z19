import importlib.util
import sys
from pathlib import Path
from typing import Callable

fp = sys.argv[1]
md = Path(sys.argv[1]).resolve()
assert md.is_file(), f"{fp} is not a file"
assert md.as_posix()[-3:] == ".py", f"{fp} is not a Python module"

spec = importlib.util.spec_from_file_location("module.name", md.as_posix())

md = importlib.util.module_from_spec(spec)
spec.loader.exec_module(md)
assert hasattr(md, "reversed2"), f"no `reversed2` in {fp}"

r = getattr(md, "reversed2")
assert isinstance(r, Callable), f"{r} is not callable"

assert r([]) == []
assert r([3, 2, 1]) == [1, 2, 3]
assert r([1, 1, 1]) == [1, 1, 1]
