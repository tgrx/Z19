import os #файл проверен с помощью fleke8

tries = 0
while tries != 100:
    name = (input("Здравствуйте, назовите свое имя: "))
    if name == "xxx":
        print("Упс, вышла ошибка при вводе данных. Повторите ваш ответ:")
    else:
        break
    tries += 1
while tries != 100:
    choice = int(input(f"{name} , какая информация вам интересна:"
                       f" первая программа новоиспеченного программиста (1),"
                       f" знакомство со мной (2)"
                       f"или информация о вашей системе(3)?"
                       f" Для выхода из программы нажмите (4). "))
    if choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("Упс, произошла ошибка при вводе данных. Повторите ваш ответ:")
        tries += 1
    else:
        if choice == 1:
            print("Hello World!")
        elif choice == 2:
            print("My name is Diana. I am 25 years old. "
                  "I'm a student of python courses in school Teach Me Skills. "
                  "My english is very bad.")
        elif choice == 3:
            print(os.name)
        else:
            print("Всего доброго!")
        break
