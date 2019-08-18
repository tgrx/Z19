a = 0
arr = [1, 2, 3, 4, 5, 6]
while True:
  try:
     a = int(input("Enter your variant (1-6): "))
  except ValueError:
     print("Variant is not an integer!")
     continue
  else:
    if a in arr:
     print("Variant is available!")
     break
    else:
     print("Variant is not 1-6!")

if a == 1:
    print("Hello world!")
if a == 2:
    print("My name is Danil, i'm 22 old, and i wanna learn python.")
if a == 3:
    import os
    print(os.name)
if a == 4:
    print("Enter your name:")
    b = str(input())
    print("Hello,", b, "!")
if a == 5:
    print("Change a variant (1-6)")
    a = int(input())
if a == 6:
    import webbrowser
    webbrowser.open('https://youtu.be/dQw4w9WgXcQ')