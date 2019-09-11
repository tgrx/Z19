import operator
from datetime import date, timedelta
from typing import Callable, Collection, Sequence, TypeVar

T = TypeVar("T")


def Reversed(sequence: Sequence):
    result = []
    for element in sequence:
        result = [element] + result
    return result


def Sorted(collection: Collection[T]):
    def partition(_sequence: Sequence[T], _low: int, _high: int):
        _i = _low - 1
        _pivot = _sequence[_high]

        for _j in range(_low, _high):
            if _sequence[_j] <= _pivot:
                _i += 1
                _sequence[_i], _sequence[_j] = _sequence[_j], _sequence[_i]
        _j = _i + 1
        _sequence[_j], _sequence[_high] = _sequence[_high], _sequence[_j]
        return _j

    def qsort(_sequence: Sequence[T], _low: int, _high: int):
        if _low < _high:
            _i = partition(_sequence, _low, _high)
            qsort(_sequence, _low, _i - 1)
            qsort(_sequence, _i + 1, _high)

    result = list(collection)
    qsort(result, 0, len(result) - 1)

    return result


def Filter(ok: Callable[[T], bool], sequence: Sequence[T]):
    return [element for element in sequence if ok(element)]


def TypedReversed(sequence: Sequence[T]):
    normal_reversed = Reversed(sequence)
    if isinstance(sequence, str):
        return "".join(str(element) for element in normal_reversed)
    return type(sequence)(normal_reversed)


def LazyReversed(sequence: Sequence[T]):
    return (_e for _e in Reversed(sequence))


class Range:
    def __init__(self, *args):
        self.start = 0
        self.stop = 0
        self.step = 1
        self.current = None

        if len(args) == 1:
            self.stop = args[0]
        elif len(args) == 2:
            self.start, self.stop = args
        elif len(args) == 3:
            self.start, self.stop, self.step = args
        else:
            raise TypeError(f"invalid number of args: {len(args)}")

        if self.step == 0:
            raise ValueError("step cannot be zero")

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        op = operator.ge if self.step > 0 else operator.le

        if op(self.current, self.stop):
            raise StopIteration

        c, self.current = self.current, self.current + self.step

        return c


class DateRange:
    cutoff = 24 * 60 * 60

    @staticmethod
    def validate_step(step: timedelta):
        if step.days < 1:
            raise ValueError(f"step must be > 1 (now: {step})")

    def __init__(self, *args):
        self.start = date.today()
        self.stop = date.today()
        self.step = timedelta(days=1)
        self.current = None

        if len(args) == 1:
            self.stop = args[0]
        elif len(args) == 2:
            self.start, self.stop = args
        elif len(args) == 3:
            self.start, self.stop, self.step = args
        else:
            raise TypeError(f"invalid number of args: {len(args)}")

        self.validate_step(self.step)

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        op = operator.ge if self.step.days > 0 else operator.le

        if op(self.current, self.stop):
            raise StopIteration

        c, self.current = self.current, self.current + self.step

        return c

    def __contains__(self, item):
        return self.start <= item < self.stop
