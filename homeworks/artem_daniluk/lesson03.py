def second_level():
    """Измерение эффективности операций над типами данных"""
    int("00001")  # 2.47 ms ± 328 µs per loop
    str(2019)  # 2.5 ms ± 360 µs per loop
    complex(2, 4)  # 2.41 ms ± 343 µs per loop
    list(str(334545))  # 2.56 ms ± 357 µs per loop
    tuple([2, 4, 6])  # 2.45 ms ± 363 µs per loop
    a = "a" * 100  # 92.1 ns ± 2.35 ns per loop
    b = 123 ** 10  # 84.8 ns ± 2.49 ns per loop
    bool(a != b)  # 482 ns ± 27.1 ns per loop
    c = 156
    d = 131
    e = 142
    bool(d < e > c)  # 651 ns ± 19.3 ns per loop
    x = [4, 2, 1]
    x += [1]
    x.sort()  # 81.1 ns ± 5.58 ns per loop
    y = (1, 3) + (4, 6)  # 81 ns ± 3.69 ns per loop
    id(y)  # 262 ns ± 27.1 ns per loop
    statistics = """Efficiency: int('00001')) = 2.47 ms ± 328 µs per loop 
            str(2019) = 2.5 ms ± 360 µs per loop       
            complex(2, 4) = 2.41 ms ± 343 µs per loop
            list(str(334545)) = 2.56 ms ± 357 µs per loop
            tuple([2, 4, 6]) = 2.45 ms ± 363 µs per loop
            a = 'a' * 100
            print(a) = 92.1 ns ± 2.35 ns per loop
            b = 123 ** 10
            print(b)  # 84.8 ns ± 2.49 ns per loop
            bool(a != b) = 482 ns ± 27.1 ns per loop
            bool(d < e > c) = 651 ns ± 19.3 ns per loop
            x = [4, 2, 1]
            x += [1]
            x.sort()
            print(x) = 81.1 ns ± 5.58 ns per loop
            y = (1, 3,) + (4, 6)
            print(y)  # 81 ns ± 3.69 ns per loop
            print(id(y))  # 262 ns ± 27.1 ns per loop             
    """
    print(statistics)


def third_level():
    """Помогает пользователю выяснить границы размеров для коллекций на компьютере"""
    while True:
        try:
            list_length = int(input("Please, input the length of the list:\t"))
            x = list()
            while list_length > 0:
                try:
                    x.append("a")
                    list_length -= 1
                except MemoryError:
                    print(
                        "Sorry, your computer can't create this list("
                    )  # примерно после 500_000_000 выдавало ошибку
                    break
        except ValueError:
            print("Error, try again!")
            continue
        else:
            if True:
                print(
                    "Okay, the length of the list is available!"
                )  # Но есть проблема: этот принт выводится даже если MemoryError(
                break


while True:
    try:
        user_choice = int(
            input(
                "Введите цифру 1 или 2, чтобы выбрать 1 или 2 задание соответсвенно:\t"
            )
        )
        if user_choice < 1 or user_choice > 2:
            raise ValueError
        break
    except ValueError:
        print("Вы должны ввести числа: 1 или 2. Попробуйте снова.\n")
if user_choice == 1:
    second_level()
else:
    third_level()
