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

reversed2 = getattr(md, "reversed2")
assert isinstance(reversed2, Callable), f"{reversed2} is not callable"

assert reversed2([]) == []
assert reversed2([3, 2, 1]) == [1, 2, 3]
assert reversed2([1, 1, 1]) == [1, 1, 1]
