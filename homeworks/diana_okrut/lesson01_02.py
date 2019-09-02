import os


while True:
    name = input("Здравствуйте, назовите свое имя: ")
    if name not in ["xxx", "yyy"]:
        break
    print("Упс, вышла ошибка при вводе данных. Повторите ваш ответ:")
    continue

while True:
    choice = int(
        input(
            f"{name} , какая информация вам интересна: первая программа новоиспеченного программиста (1),"
            f" знакомство со мной (2) или информация о вашей системе(3)? Для выхода из программы нажмите (4). "
        )
    )
    if choice in range(1, 5):
        break
    print("Упс, вышла ошибка при вводе данных. Повторите ваш ответ:")
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
else:
    print("Всего доброго!")