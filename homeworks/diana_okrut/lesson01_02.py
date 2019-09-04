import os


name = input("Здравствуйте, назовите свое имя: ")
while True:
    try:
        choice = int(
            input(
                f"{name} , какая информация вам интересна: первая программа новоиспеченного программиста (1),"
                f" знакомство со мной (2) или информация о вашей системе(3)? Для выхода из программы нажмите (4). "
            )
        )
    except ValueError:
        print("Только числа!")
        continue
    if choice in range(1, 5):
        break
    print("Только от 1 до 4!")
    continue

if choice == 1:
    print("Hello World!")
elif choice == 2:
    print(
        "My name is Diana. I am 25 years old. I'm a student of python courses in school Teach Me Skills."
        " My english is very bad."
    )
elif choice == 3:
    print(os.name)
elif choice == 4:
    print("Всего доброго!")
