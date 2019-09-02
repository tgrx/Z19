from verification import verification
import webbrowser
import os


a = verification()
if a == 1:
    print("Hello world!")
if a == 2:
    print("My name is Danil, i'm 22 old, and i wanna learn python.")
if a == 3:
    print(os.name)
if a == 4:
    print("Enter your name:")
    b = str(input())
    print("Hello,", b, "!")
if a == 5:
    print("Change a variant (1-6)")
    a = int(input())
if a == 6:
    webbrowser.open("https://youtu.be/dQw4w9WgXcQ")
    print("Bye world!")
