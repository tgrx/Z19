## Уровень 2


a = [1,2,3,4,5]

print(list(reversed(a)))

## Уровень 3

b = [2, 4, 7, 1, 3, 5, 6]

print(list(sorted(b)))

## Уровень 4

 def is_leap(year: int):
  """Проверяет, високосный ли год"""
  if year % 400 == 0:
            return True
    if year % 100 == 0:
       return False
    if year % 4 == 0:
      return True
   return False

years = [2000,2004,2019]
x = filter(is_leap, years)
print(list(x))

bool