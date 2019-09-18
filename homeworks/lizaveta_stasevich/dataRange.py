import operator
from datetime import date as d, timedelta as t


class DateRange:
    cutoff = 24 * 60 * 60

    @staticmethod
    def validate_step(step: t):
        if step.days < 1:
            raise ValueError(f"step must be > 1 (now: {step})")

    def __init__(self, *args):
        self.start = d.today()
        self.stop = d.today()
        self.step = t(days=1)
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
