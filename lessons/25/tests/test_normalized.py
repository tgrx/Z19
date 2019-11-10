from pathlib import Path
from random import choice
from string import ascii_lowercase
from typing import Callable

wanted_name = "normalized"


def wants_path(pth: Path) -> bool:
    return "lesson25" in pth.name


def wants_module(_module):
    return True


def verify(module):
    assert hasattr(module, wanted_name), f"no `{wanted_name}` defined in {module}"

    normalized = getattr(module, wanted_name)

    assert isinstance(normalized, Callable), f"`{wanted_name}` is not callable"

    a, b, c, d, e, f, g = [
        "".join(choice(ascii_lowercase) for _ in range(4)) for _ in range(7)
    ]

    checks = {
        "": "",
        f".": "",
        f"..": "",
        f"../../../..": "",
        f"../{d}": f"/{d}",
        f"../{d}/": f"/{d}/",
        f"./../../../../": "/",
        f"./{f}/./././././{f}/..": f"{f}",
        f"/../../../..": "",
        f"/../../../../": "/",
        f"/../../../../.": "",
        f"/.././.././../{f}/.././.././../{f}/": f"/{f}/",
        f"/../{d}": f"/{d}",
        f"/../{d}/": f"/{d}/",
        f"/{a}": f"/{a}",
        f"/{a}/": f"/{a}/",
        f"/{a}/{b}/./../{c}": f"/{a}/{c}",
        f"/{a}/{b}/./{a}/": f"/{a}/{b}/{a}/",
        f"/{a}/{c}/../{b}/": f"/{a}/{b}/",
        f"/{b}": f"/{b}",
        f"/{c}/": f"/{c}/",
        f"/{e}/./": f"/{e}/",
        f"/{e}/{e}": f"/{e}/{e}",
        f"/{f}/../../../../{f}": f"/{f}",
        f"/{f}/../../{f}": f"/{f}",
        f"/{g}/{a}/../{b}": f"/{g}/{b}",
        f"{a}": f"{a}",
        f"{a}/": f"{a}/",
        f"{a}/{b}/{c}/{d}/{e}/{f}": f"{a}/{b}/{c}/{d}/{e}/{f}",
    }

    for test_data, expected in checks.items():
        try:
            got = normalized(test_data)
        except Exception as err:
            import traceback

            tb = traceback.format_exc().replace("\n", " \ ")
            got = f"ERROR: {err} ({tb})"

        assert got == expected, (
            f'fail: {wanted_name}("{test_data}")'
            f'\n\texpected: "{expected}"'
            f'\n\tgot:      "{got}"'
        )
