# 1 выводит "Hello, World"

print("Hello, world!")

# 2 выводит информацию о вас

name = input("Input your name - ")
surname = input("Input your surname - ")
age = input("Input your age - ")
print("Information about user: ", name, surname, ",", age, "years.")

# 3 выводит информацию о системе, на которой она будет запущена

import platform

print("Platform: ", platform.platform())
print("System: ", platform.system())
print("Release: ", platform.release())
print("Version: ", platform.version())

# 4 спрашивает имя у пользователя и приветствует его

print("Hello,", name)

# 5 спрашивает вариант у пользователя и выводит один из вариантов выводов выше

option = int(
    input(
        "Choose the option: 1)'a cup of coffee' or 2)'a cup of tea' or 3)'rumka vodki na stole'"
    )
)
if option == 1:
    print("You have chosen a cup of coffee.")
elif option == 2:
    print("Your choice is a cup of tea.")
elif option == 3:
    print("Oh, it's OK, you're not an alcoholic:)")
else:
    print("Wrong number!")

# 6 всё, на что вы способны за время до следующего занятия
# определяет високосный год

year = int(input("Input the year - "))
if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
    print("The year", year, "is not a leap year.")
else:
    print("The year", year, "is a leap year.")
