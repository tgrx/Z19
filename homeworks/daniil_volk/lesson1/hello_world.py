from verification import verification
import webbrowser
import os


print("Enter variant:")
variant = verification(1, 7)
if variant == 1:
    print("Hello world!")
if variant == 2:
    print("My name is Danil, i'm 22 old, and i wanna learn python.")
if variant == 3:
    print(os.name)
if variant == 4:
    print("Enter your name :")
    b = str(input())
    print("Hello,", b, "!")
if variant == 5:
    print("Change a variant (1-6)")
    variant = int(input())
if variant == 6:
    webbrowser.open("https://youtu.be/dQw4w9WgXcQ")
