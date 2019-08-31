import importlib.util
import multiprocessing
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

HOMEWORKS_DIR = PROJECT_DIR / "homeworks"
LESSONS_DIR = PROJECT_DIR / "lessons"


def _import(module_path: Path, prefix=""):
    package_name = module_path.parent.name
    module_name = module_path.name[:-3]

    spec = importlib.util.spec_from_file_location(
        f"{prefix}.{package_name}.{module_name}", module_path.as_posix()
    )

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    return module


class Runner(multiprocessing.Process):
    def run(self) -> None:
        for test_path in LESSONS_DIR.glob("**/test_*.py"):
            print(f"\nrun test: {test_path.as_posix()}\n")

            test = _import(test_path, "tests")

            for homework_path in HOMEWORKS_DIR.glob("**/*.py"):
                print(f"\n\tcheck homework in {homework_path.as_posix()}")

                if not test.wants_path(homework_path):
                    print(f"\t\tskip: test does not want path")
                    continue

                hm = _import(homework_path, "hw")

                if not test.wants_module(hm):
                    print(f"\t\tskip: test does not want module")
                    continue

                test.verify(hm)

                print("\tok")

        print("END test run\n\n")


def main():
    r = Runner()
    r.start()
    r.join(5)
    assert r.exitcode == 0, "tests failed"


if __name__ == "__main__":
    main()
