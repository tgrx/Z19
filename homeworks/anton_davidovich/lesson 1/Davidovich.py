import platform

name = input("name: ")
print(f"Hello, {name}")

while True:
    try:
        choose = int(input("выбирите вариант: 1, 2,3 "))
    except ValueError:
        print("Только числа!")
        continue
    if choose in range(1, 4):
        break
    print("Только от 1 до 3!")
    continue

if choose == 1:
    print("hello world")
elif choose == 2:
    print("Меня зовут Антон - я продовец техники xiaomi")
elif choose == 3:
    print(f"system: {platform.system()} ")
else:
    print("Вели не правильный вариант")
