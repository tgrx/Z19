print("Hello, World!!!\nI am HAL 9000")
import os

print("I work on a system " + os.name)
name = input("What's your name? \n")
print("Hello " + name + "!\nWhat do you want to do?")
answer = input("Would you like to program? \n")
if answer == "yes":  # выбор варианта ответа
    print("Good! " + name)
if answer == "no":
    print("I'm sorry")
else:
    print("I did not understand the answer")
