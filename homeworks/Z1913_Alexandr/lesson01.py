print("Hello, World!!!\nI am HAL 9000")
import os

print("I work on a system " + os.name)
name = input("What's your name? \n")
print("Hello " + name + "!\nWhat do you want to do?")
answer = input("Would you like to program? \n")
if answer == "yes" or answer == "Yes" or answer == "YES":  # выбор варианта ответа с проверкой регистра
    print("Good! " + name)
elif answer == "no" or answer == "No" or answer == "NO":
    print("I'm sorry")
else:
    print("I did not understand the answer")  # если ответ не да ни нет
