d = input("Здравствуйте. Назовите свое имя: ")
e = int(input("Какая информация вам интересна: первая программа новоиспеченного программиста (1),"\
              " знакомство со мной (2) или информация о моем железе(3)?"))
if e == 1 :
     print("Hello World!")
elif e == 2 :
     print("My name is Diana. I am 25 years old. I am a student of python courses in school Teach Me Skills. " \
    "My english is very bad.")
elif e == 3 :
     print("Я буду использовать для работы  64-разрядную ОС Windows 10 pro. " \
    "Процессор Intel Core i7 - 6700 HQ CPU @ 2.60 GHz 2.6 GHz и 8 GB ОЗУ")
else: print("Некорректные данные")
