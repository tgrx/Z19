#1. выводит "Hello, World"
print('Hello, world!')

#2. выводит информацию о вас
user_name = input('Введите Ваше имя:\n')
user_surname = input('Введите Вашу фамилию:\n')
user_age = int(input('Введите Ваш возраст:\n'))
print("Вас зовут:", user_name, user_surname, ", Ваш возраст: ", user_age)

#3. выводит информацию о системе, на которой она будет запущена
import platform
print("Platform:", platform.platform())
print("System:", platform.system())
print("Release:", platform.release())
print("Version:", platform.version())

#4. спрашивает имя у пользователя и приветствует его
user_name = input('Как Вас зовут?\n')
print("Привет,", user_name,"!")

#5. спрашивает вариант у пользователя и выводит один из вариантов выводов выше
user_choice = int(input('Please, choose one of three options: 1)Windows, 2)Linux, 3)Mac\n'))
if user_choice == 1:
    print('Your choice is Windows')
elif user_choice == 2:
    print('Your choice is Linux')
elif user_choice == 3:
    print('Your choice is Mac')
else:
    print('Wrong number!')

#6. покажите всё, на что вы способны за время до следующего занятия
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