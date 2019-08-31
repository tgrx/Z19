import sys
from os import system
from webbrowser import open

print("\tЗдравствуйте! Что бы вы хотели сделать?\n")
print("\t1 -- Вывести Hello, World!")
print("\t2 -- Вывести информацию обо мне")
print("\t3 -- Вывести информацию о системе")
print("\t4 -- Вывести приветстие с вашим именем")
print("\t5 -- Выйти из программы\n")

while True:
    try:
        number = int(input("\tЧто выбираете?\t\t"))
        if number < 1 or number > 5:
            raise ValueError
        break
    except ValueError:
        print("\nВы должны ввести число от 1 до 5. Попробуйте снова.\n")

if number == 1:
    print("\n\tHello, World!\n")
elif number == 2:
    answer = str(
        input(
            "\n\tПривет! Меня зовут Алина. Мне 19 лет. Я учусь в БГУИРе. Интересует?)\n"
        )
    )
    ans = answer.lower()
    if ans == "да":
        open("https://vk.com/ageevaalina")
    else:
        print("Очень жаль")
elif number == 3:
    platform = sys.platform
    if platform == "win32":
        system("SYSTEMINFO")
    else:
        print("\nВаша система -- ", platform)
elif number == 4:
    name = str(input("\n\tКак вас зовут?\t\t"))
    print("\n\tДобрый вечер, ", name, "! Мы рады нашему знакомству!")
elif number == 5:
    print("\nВсего доброго!\n")
    exit()
