# from datetime import timedelta as t
#
#
# def Reversed(x):
#     x = list(x)
#     l = len(x)
#     steps = l // 2
#     for i in range(steps):
#         l -= 1
#         x[i], x[l] = x[l], x[i]
#     return x
#
#
# def Sorted(x):
#     x = list(x)
#     l = len(x)
#     for i in range(l):
#         for j in range(l - 1):
#             if x[j] > x[j + 1]:
#                 x[j + 1], x[j] = x[j], x[j + 1]
#     return x
#
#
# def Filter(pred, old_list):
#     new_list = []
#     for x in old_list:
#         if pred(x):
#             new_list.append(x)
#     return new_list
#
#
# def TypedReversed(x):
#     typex = type(x)
#     x = list(x)
#     l = len(x)
#     steps = l // 2
#     for i in range(steps):
#         l -= 1
#         x[i], x[l] = x[l], x[i]
#     if typex == list:
#         return x
#     elif typex == tuple:
#         return tuple(x)
#     elif typex == str:
#         z = ""
#         for c in range(len(x)):
#             z += str(x[c])
#         return z
#
#
# def LazyReversed(x):
#     if not isinstance(x, (str, tuple, list)):
#         return
#     x = list(x)
#     l = len(x)
#     steps = l // 2
#     for i in range(steps):
#         l -= 1
#         x[i], x[l] = x[l], x[i]
#     return iter(x)


class Range:
    def __init__(self, start, stop="default", step="default"):
        if step == "default":
            self.step = 1
            self.start = start
            self.stop = stop
            self.current = start
        if stop == "default":
            self.stop = start
            self.start = 0
            self.step = 1
            self.current = start
        if stop != "default" and step != "default":
            self.start = start
            self.stop = stop
            self.step = step
            self.current = start
        check = self.start
        if not isinstance(check, (str, tuple, list)):
            return

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.stop >= self.start and self.step < 0:
            raise StopIteration
        if self.stop <= self.start and self.step > 0:
            raise StopIteration
        if self.start < self.stop:
            if self.current >= self.stop:
                raise StopIteration
            c, self.current = self.current, self.current + self.step
            return c
        elif self.start > self.stop:
            if self.current <= self.stop:
                raise StopIteration
            c, self.current = self.current, self.current + self.step
            return c


#
#
# print(list(Range(3)) == [0, 1, 2])
# print(tuple(Range(-1, 2)) == (-1, 0, 1))
# print(tuple(Range(0, -10, -2)) == (0, -2, -4, -6, -8))
# print(list(Range(0, -10, 3)) == [])
# print(list(Range(10, -10, -1)))
# print(list(Range(-10, 10, 1)))
#
# class DateRange:
#     def __init__(self, start, stop="default", step="default"):
#         if step == "default":
#             self.step = 1
#             self.start = start
#             self.stop = stop
#             self.current = start
#         if stop == "default":
#             self.stop = start
#             self.start = 0
#             self.step = 1
#             self.current = start
#         if stop != "default" and step != "default":
#             self.start = start
#             self.stop = stop
#             self.step = step
#             self.current = start
#
#     def __iter__(self):
#         self.current = self.start
#         return self
#
#     def __next__(self):
#         if self.stop >= self.start and self.step < 0:
#             raise StopIteration
#         if self.stop <= self.start and self.step > 0:
#             raise StopIteration
#         if self.start < self.stop:
#             if self.current >= self.stop:
#                 raise StopIteration
#             c, self.current = self.current, self.current + t(self.step)
#             return c
#         elif self.start > self.stop:
#             if self.current <= self.stop:
#                 raise StopIteration
#             c, self.current = self.current, self.current + t(self.step)
#             return c
