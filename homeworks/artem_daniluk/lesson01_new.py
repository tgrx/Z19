import platform


def first_task():
    print("Hello, world!")


user_name = input("Введите Ваше имя:\n")
user_surname = input("Введите Вашу фамилию:\n")
while True:
    try:
        user_age = int(input("Введите Ваш возраст:\n"))
        if type(user_age) == int:
            break
    except ValueError:
        print("Ошбика, введите возраст заново!")
        continue


def second_task():
    """Спрашивает данные пользователя(имя, фамилия, возраст)."""
    print(f"Вас зовут: {user_name} {user_surname}, Ваш возраст: {user_age}")


def third_task():
    """Выводит информацию о системе пользователя"""

    print(f"Platform: {platform.platform()}")
    print(f"System: {platform.system()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")


def fourth_task():
    """Приветствует пользователя"""
    print(f"Привет,{user_name}!")


def fifth_task():
    """Даёт пользователю выбрать одну из трех предлагаемых систем"""
    while True:
        try:
            user_choice = int(
                input(
                    "Please, choose one of three options: 1)Windows, 2)Linux, 3)Mac\n"
                )
            )
            if user_choice == 1:
                print("Your choice is Windows")
                break
            elif user_choice == 2:
                print("Your choice is Linux")
                break
            elif user_choice == 3:
                print("Your choice is Mac")
                break
            else:
                print("Wrong number!")
                continue
        except ValueError:
            print("Error, try again!")
            continue


def sixth_task():
    """что-то похожее на калькулятор"""
    while True:
        try:
            first_number = int(input("Введите первое число.\n"))
            second_number = int(input("Введите второе число.\n"))
            math_sign = input("Введите математический знак.\n")
            if math_sign == "+":
                result = first_number + second_number
                print(result)
                break
            elif math_sign == "-":
                result = first_number - second_number
                print(result)
                break
            elif math_sign == "*":
                result = first_number * second_number
                print(result)
                break
            elif math_sign == "/":
                result = first_number / second_number
                print(result)
                break
            elif math_sign == "**":
                result = pow(first_number, second_number)
                print(result)
                break
            elif math_sign == "//":
                result = first_number // second_number
                print(result)
            elif math_sign == "%":
                result = first_number % second_number
                print(result)
                break
            else:
                print("Неверный знак")
        except ValueError:
            print("Error, try again!")
            continue


while True:
    try:
        user_wish = int(input("Choose 1 of 6 tasks you want to run. Enter 0 to exit\n"))
        if user_wish == 1:
            first_task()
        elif user_wish == 2:
            second_task()
        elif user_wish == 3:
            third_task()
        elif user_wish == 4:
            fourth_task()
        elif user_wish == 5:
            fifth_task()
        elif user_wish == 6:
            sixth_task()
        elif user_wish == 0:
            break
        else:
            print("Wrong number!")
    except ValueError:
        print("Error, try again!")
        continue
