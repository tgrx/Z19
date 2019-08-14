import os

print("\tЗдравствуйте! Что бы вы хотели сделать?\n")
print("\t1 -- Вывести Hello, World!")
print("\t2 -- Вывести информацию обо мне")
print("\t3 -- Вывести информацию о системе")
print("\t4 -- Вывести приветстие с вашим именем")
number = int(input("\tЧто выбираете?\t\t"))

if number == 1:
    print("\n\tHello, World!\n")
elif number == 2:
    print("\n\tПривет! Меня зовут Алина. Мне 19 лет. Я учусь в БГУИРе. Интересует?)\n")
elif number == 3:
    def SYSTEMINFO():
        os.system("SYSTEMINFO")

    SYSTEMINFO()
elif number == 4:
    name = str(input("\n\tКак вас зовут?\t\t"))
    print("\n\tДобрый вечер, ", name, "! Мы рады нашему знакомству!")
else:
    print("\tВы ввели неверное значение")
