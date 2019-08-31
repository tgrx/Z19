import os

print("Hello, World!!!\nI am HAL 9000")
print("I work on a system " + os.name)
name = input("What's your name? \n")
print("Hello " + name + "!\nWhat do you want to do?")
i = 0
while i != 1:  # цикл пока не получим ответ да или нет в зависимости от регистра
    answer = input("Would you like to program? \n")
    if answer == "yes" or answer == "Yes" or answer == "YES":  # выбор варианта ответа с проверкой регистра
        print("Good! " + name)
        i = 1
    elif answer == "no" or answer == "No" or answer == "NO":
        print("I'm sorry")
        i = 1
    else:
        print("I did not understand the answer")  # если ответ не да ни нет
        i = 0
