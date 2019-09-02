import os

print("Hello, World!!!\nI am HAL 9000")
print("I work on a system " + os.name)
name = input("What's your name? \n")
print("Hello " + name + "!\nWhat do you want to do?")

while 1:
    answer = input("Would you like to program? \n")
    if answer.lower() == "yes":
        print(f"Good! {name}")
        break
    elif answer.lower() == "no":
        print("I'm sorry!")
        break
    else:
        print("I did not understand the answer!")
        continue

