import os
d = input("Здравствуйте, назовите свое имя: ")
print(d, ", приятно познакомиться!")
e = int(input("Какая информация вам интересна: первая программа новоиспеченного программиста (1), знакомство со мной (2)"
              " или информация о вашей системе(3)?"))
#хотела сделать вот так,.e = int(input(d, "Какая информация вам интересна: первая программа новоиспеченного программиста
# (1), знакомство со мной (2) или информация о моем железе(3)?"))
if e == 1:
    print("Hello World!")
elif e == 2:
    print("My name is Diana. I am 25 years old. I am a student of python courses in school Teach Me Skills. "
          "My english is very bad.")
elif e == 3:
    print(os.name())
else:
    print("Некорректные данные")
