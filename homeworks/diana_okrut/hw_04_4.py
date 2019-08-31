def A(m, n):
    try:
        if m == 0:
            return n + 1
        if m > 0:
            if n == 0:
                return A(m - 1, 1)
            else:
                return A(m - 1, A(m, n - 1))
    except TypeError:
        return "kek"
    except RecursionError:
        return "Maximum recursion depth exceeded in comparison."

# In [87]: A(3, 8)
# Out[87]: 2045
