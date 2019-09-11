import operator
from collections import defaultdict
from decimal import Decimal
from itertools import chain
from timeit import timeit
from typing import Dict

INT_1 = 5 ** 7
INT_2 = 7 ** 5

LONG_1 = 17 ** 19
LONG_2 = 19 ** 17

FLOAT_1 = 1e30
FLOAT_2 = 1e-30

COMPLEX_1 = 1 + 2j
COMPLEX_2 = 2 - 1j

DECIMAL_INT_1 = Decimal(INT_1)
DECIMAL_INT_2 = Decimal(INT_2)

DECIMAL_LONG_1 = Decimal(LONG_1)
DECIMAL_LONG_2 = Decimal(LONG_2)

DECIMAL_FLOAT_1 = Decimal("0.33")
DECIMAL_FLOAT_2 = Decimal("1.66")

N = 10000

STR = ("ab" * (N // 4)) + "c" + ("ab" * (N // 4 - 1)) + "d"
LIST = [_i for _i in range(N)]
TUPLE = tuple(_i for _i in range(N))
SET = {_i for _i in range(N)}
DICT = {_i: _i for _i in range(N)}
RANGE = range(N)

BENCHMARKS_NUMBERS = {
    "addition": {
        "int": (INT_1, INT_2),
        "long": (LONG_1, LONG_2),
        "float": (FLOAT_1, FLOAT_2),
        "complex": (COMPLEX_1, COMPLEX_2),
        "decimal/int": (DECIMAL_INT_1, DECIMAL_INT_2),
        "decimal/long": (DECIMAL_LONG_1, DECIMAL_LONG_2),
        "decimal/float": (DECIMAL_FLOAT_1, DECIMAL_FLOAT_2),
    },
    "multiplication": {
        "int": (INT_1, INT_2),
        "long": (LONG_1, LONG_2),
        "float": (FLOAT_1, FLOAT_2),
        "complex": (COMPLEX_1, COMPLEX_2),
        "decimal/int": (DECIMAL_INT_1, DECIMAL_INT_2),
        "decimal/long": (DECIMAL_LONG_1, DECIMAL_LONG_2),
        "decimal/float": (DECIMAL_FLOAT_1, DECIMAL_FLOAT_2),
    },
    "division": {
        "int": (INT_1, INT_2),
        "long": (LONG_1, LONG_2),
        "float": (FLOAT_1, FLOAT_2),
        "complex": (COMPLEX_1, COMPLEX_2),
        "decimal/int": (DECIMAL_INT_1, DECIMAL_INT_2),
        "decimal/long": (DECIMAL_LONG_1, DECIMAL_LONG_2),
        "decimal/float": (DECIMAL_FLOAT_1, DECIMAL_FLOAT_2),
    },
}

BENCHMARKS_SEARCH = {
    "first": {
        "str": (STR, "a"),
        "list": (LIST, 0),
        "tuple": (TUPLE, 0),
        "set": (SET, 0),
        "dict": (DICT, 0),
        "range": (RANGE, 0),
    },
    "middle": {
        "str": (STR, "c"),
        "list": (LIST, 5000),
        "tuple": (TUPLE, 5000),
        "set": (SET, 5000),
        "dict": (DICT, 5000),
        "range": (RANGE, 5000),
    },
    "last": {
        "str": (STR, "d"),
        "list": (LIST, 9999),
        "tuple": (TUPLE, 9999),
        "set": (SET, 9999),
        "dict": (DICT, 9999),
        "range": (RANGE, 9999),
    },
    "outbound": {
        "str": (STR, "x"),
        "list": (LIST, 10000),
        "tuple": (TUPLE, 10000),
        "set": (SET, 10000),
        "dict": (DICT, 10000),
        "range": (RANGE, 10000),
    },
}

OPERATORS_MAP = {
    "addition": operator.add,
    "division": operator.truediv,
    "first": operator.contains,
    "last": operator.contains,
    "middle": operator.contains,
    "multiplication": operator.mul,
    "outbound": operator.contains,
}


def run(benchmarks: Dict) -> Dict:
    measurements = defaultdict(dict)

    for benchmark, data_set in benchmarks.items():
        op = OPERATORS_MAP[benchmark]

        for type_name, args in data_set.items():
            timing = timeit("op(*args)", globals=locals(), number=10000)

            measurements[benchmark][type_name] = timing

    return dict(measurements)


def normalize(measurements: Dict) -> Dict:
    normalized = defaultdict(dict)

    min_timing_global = min(chain(*[_i.values() for _i in measurements.values()]))

    for benchmark, types_timings in measurements.items():
        min_timing_benchmark = min(types_timings.values())

        for type_name, timing in types_timings.items():
            normalized[benchmark][type_name] = (
                timing / min_timing_benchmark,
                timing / min_timing_global,
            )

    return dict(normalized)


def display(measurements):
    for benchmark, types_timings in sorted(measurements.items()):
        print(f"\n[ {benchmark} ]")

        sorted_timings = sorted(types_timings.items(), key=lambda _i: _i[-1])

        for type_name, (timing_type, timing_benchmark) in sorted_timings:
            print(f"\t{type_name:<20}\t{timing_type:>10.2f}\t{timing_benchmark:>10.2f}")

    print()


def main():
    for benchmark in (BENCHMARKS_NUMBERS, BENCHMARKS_SEARCH):
        measurements = run(benchmark)
        normalized = normalize(measurements)
        display(normalized)


if __name__ == "__main__":
    main()
