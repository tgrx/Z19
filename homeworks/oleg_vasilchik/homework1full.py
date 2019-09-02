import os

# Продолжение домашки 1
print("Привет, Мир!\nЯ Lenovo IdeaPad, в твоём распоряжении")

print("Я работаю на системе - " + os.name)

name = input("Kак тебя зовут? : ")
print("Привет, " + name)

x = input("Сколько будет 2+2? : ")

if int(x) == 4:
    print("Ты прав, получай 10 за домашку")
else:
    print("Попробуй еще раз")
