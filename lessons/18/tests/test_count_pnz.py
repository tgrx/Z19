from decimal import Decimal
from pathlib import Path
from random import randint
from typing import Callable, NamedTuple

wanted_name = "count_pnz"


def wants_path(pth: Path) -> bool:
    return "lesson18" in pth.name


def wants_module(_module):
    return True


class PNZ(NamedTuple):
    p: int
    n: int
    z: int
    N: int


def gen_pnz() -> PNZ:
    p = randint(0, 10)
    n = randint(0, 10)
    z = randint(0, 10)

    return PNZ(p=p, n=n, z=z, N=Decimal(p + n + z))


def verify(module):
    assert hasattr(module, wanted_name), f"no `{wanted_name}` defined in {module}"

    f = getattr(module, wanted_name)

    assert isinstance(f, Callable), f"`{wanted_name}` is not callable"

    checks = {
        (): ("0.000000", "0.000000", "0.000000"),
        (-1,) * 13 + (1,) * 10 + (0,) * 6: ("0.344828", "0.448276", "0.206897"),
    }

    checks.update(
        {
            ((1,) * w.p + (-1,) * w.n + (0,) * w.z): (
                f"{w.p / w.N:.6f}" if w.N else "0.000000",
                f"{w.n / w.N:.6f}" if w.N else "0.000000",
                f"{w.z / w.N:.6f}" if w.N else "0.000000",
            )
            for w in (gen_pnz() for _ in "0123456789")
        }
    )

    for origin, expected in checks.items():
        got = f(origin)
        assert (
            got == expected
        ), f"{wanted_name}({origin!r}) != {expected!r}: returned {got!r}"
