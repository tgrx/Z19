def first_task():
    print('Hello, world!')


def second_task(user_name, user_surname, user_age):
    """Спрашивает данные пользователя(имя, фамилия, возраст)."""
    user_name = input('Введите Ваше имя:\n')
    user_surname = input('Введите Вашу фамилию:\n')
    user_age = int(input('Введите Ваш возраст:\n'))
    print("Вас зовут:", user_name, user_surname, ", Ваш возраст: ", user_age)


def third_task():
    """Выводит информацию о системе пользователя"""
    import platform
    print("Platform:", platform.platform())
    print("System:", platform.system())
    print("Release:", platform.release())
    print("Version:", platform.version())


def fourth_task(user_name):
    """Приветствует пользователя"""
    user_name = input('Как Вас зовут?\n')
    print("Привет,", user_name, "!")


def fifth_task(user_choice):
    """Даёт пользователю выбрать одну из трех предлагаемых систем"""
    user_choice = int(input('Please, choose one of three options: 1)Windows, 2)Linux, 3)Mac\n'))
    if user_choice == 1:
        print('Your choice is Windows')
    elif user_choice == 2:
        print('Your choice is Linux')
    elif user_choice == 3:
        print('Your choice is Mac')
    else:
        print('Wrong number!')


def sixth_task(first_number, second_number, math_sign, result):
    """что-то похожее на калькулятор"""
    first_number = int(input('Введите первое число.\n'))
    second_number = int(input('Введите второе число.\n'))
    math_sign = input('Введите математический знак.\n')
    if math_sign == '+':
        result = first_number + second_number
        print(result)
    elif math_sign == '-':
        result = first_number - second_number
        print(result)
    elif math_sign == '*':
        result = first_number * second_number
        print(result)
    elif math_sign == '/':
        result = first_number / second_number
        print(result)
    elif math_sign == '**':
        result = pow(first_number, second_number)
        print(result)
    elif math_sign == '//':
        result = first_number // second_number
        print(result)
    elif math_sign == '%':
        result = first_number % second_number
        print(result)
    else:
        print('Неверный знак')


user_wish = int(input("Choose 1 of 6 tasks you want to run.\n"))
if user_wish == 1:
    first_task()
elif user_wish == 2:
    second_task('Artem', 'Danilyuk', '18')
elif user_wish == 3:
    third_task()
elif user_wish == 4:
    fourth_task('Artem')
elif user_wish == 5:
    fifth_task('1')
elif user_wish == 6:
    sixth_task('15', '12', '+', '27')
else:
    print('Wrong number!')
