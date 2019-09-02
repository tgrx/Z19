import platform

# print("hello world")
# print("асталовиста бейби")
# print("system:", platform.system())

name = (input("name: "))
print(f"Hello, {name}")
choise = int(input("выбирите вариант: 1, 2,3 "))
if choise == 1:
    print("hello world")
elif choise == 2:
    print("Меня зовут Антон - япродовец техники xiaomi")
elif choise == 3:
    print("system:", platform.system())
else:
    print("Вели не правильный вариант")
