# Ответы на вопросы

## Есть ли массив (array) в Python?

1. массив чисел: [array](https://docs.python.org/3/library/array.html)
1. массив байт: [bytearray](https://docs.python.org/3/library/stdtypes.html#bytearray)
1. [`numpy.array`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.array.html)

## Как внутри устроена функция?

```python
def A(m, n):
    if m == 0:
        return n + 1
    if m > 0:
        if n == 0:
            return A(m - 1, 1)
        else:
            return A(m - 1, A(m, n - 1))
```

Байткод:

```python
from dis import dis
dis(A)
```

Код в двоичном виде:

```python
A.__code__.co_code
```
