test_data = [
    [5 ** 7, 7 ** 5, "int"],
    [17 ** 19, 19 ** 17, "int"],
    [1e30, 1e-30, "float"],
    [1 + 2j, 2 - 1j, "complex"],
    [0.33, 1.66, "decimal"],
    [5 ** 7, 7 ** 5, "decimal"],
    [17 ** 19, 19 ** 17, "decimal"],
]
operation = [["add", "+"], ["multiple", "*"], ["division", "/"]]
