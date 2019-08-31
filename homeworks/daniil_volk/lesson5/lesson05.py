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
# def Filter(y, x):
#     x = list(x)
#     l = len(x)
#     z = []
#     if isinstance(y, bool):
#         if y is True:
#             for i in range(l):
#                 if x[i] > 0:
#                     z.append(x[i])
#             return (z)
#         else:
#             for i in range(l):
#                 if x[i] == 0:
#                     z.append(x[i])
#             return z
#     else:
#         y = str(y)
#         for i in range(l):
#             if y in x[i]:
#                 z.append(x[i])
#         return z
#
#
# def TypedReversed(x):
#     typex = type(x)
#     print(typex)
#     if typex == dict:
#         raise Exception('Dict')
#     x = list(x)
#     l = len(x)
#     steps = l // 2
#     for i in range(steps):
#         l -= 1
#         x[i], x[l] = x[l], x[i]
#     if typex == set:
#         return set(x)
#     elif typex == tuple:
#         return tuple(x)
#     elif typex == list:
#         return list(x)
#     elif typex == frozenset:
#         return frozenset(x)
#     elif typex == str:
#         x = str(x)
#         x = x.replace("'", "")
#         x = x.replace(", ", "")
#         x = x.replace("[", "")
#         x = x.replace("]", "")
#         return str(x)
#
#
# class Range:
#     def __init__(self, start, stop='default', step='default'):
#         if step == 'default':
#             self.step = 1
#             self.start = start
#             self.stop = stop
#             self.current = start
#         if stop == 'default':
#             self.stop = start
#             self.start = 0
#             self.step = 1
#             self.current = start
#         if stop != 'default' and step != 'default':
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
#             c, self.current = self.current, self.current + self.step
#             return c
#         elif self.start > self.stop:
#             if self.current <= self.stop:
#                 raise StopIteration
#             c, self.current = self.current, self.current + self.step
#             return c
#
#
# class DateRange:
#     def __init__(self, start, stop='default', step='default'):
#         if step == 'default':
#             self.step = 1
#             self.start = start
#             self.stop = stop
#             self.current = start
#         if stop == 'default':
#             self.stop = start
#             self.start = 0
#             self.step = 1
#             self.current = start
#         if stop != 'default' and step != 'default':
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
