# ООП

Наверное, самая популярная парадигма (более 99%)
в современном программировании.

Википедия:
[ООП](https://ru.wikipedia.org/wiki/%D0%9E%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%BD%D0%BE-%D0%BE%D1%80%D0%B8%D0%B5%D0%BD%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%BD%D0%BE%D0%B5_%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5).

Сто тысяч миллионов видео, курсов и ссылок
в [интернете](https://www.google.com/search?q=ООП).

Суть: объединяем и данные, и способ обработки этих данных
в одну сущность.

В Python такая сущность называется
["класс"](https://docs.python.org/3/tutorial/classes.html).

А "данные" и "способ обработки этих данных" —
когда они внутри класса — имею название: "атрибуты".

## Пример

Напишем свой собственный класс.

"Данные" — пусть это будет шаблонная строка
с фальшивым приветствием.

А "способом обработки этих данных"
пусть будет заполнение этой шаблонной строки
каким-то именем.

```python
class Noname:
    # данные:
    data = "Привет, {username}! Рад знакомству!"

    # способ, который с данными что-то делает:
    def say_hello(self, tykto: str) -> str:
        return self.data.format(username=tykto)
```
 
Прекрасный и функциональный класс!

### Что это даёт и как этим пользоваться

Пользоваться классами очень просто:

 ```python
n = Noname()
r = n.say_hello("анон")
print(r)
# видим: "Привет, анон! Рад знакомству!"
```

## Пространство имён

Класс задаёт, кроме всего прочего, пространство имён.
Это означает, что:
1. атрибуты класса видны классу, а внешнему миру нет:
    ```python
    print(data)  # NameError
    say_hello("xxx")  # NameError
    ```
1. если нужно во внешнем мире получить доступ к атрибуту класса, используется синтаксис "через точку"
    ```python
    class Hater:
        data = "Ненавижу тебя, {username}!"

    print(Noname.data)  # "Привет, {username}! Рад знакомству!"
    Noname.say_hello(Hater, "анон")  # "Ненавижу тебя, анон!"
    ```

## Тип

Класс определяет, кроме всего прочего, новый тип.

Условно, класс == тип.

```python
class Anon:
    def say_hello(self):
        return "Anonim legion"

class Deanon:
    def say_hello(self):
        return "127.0.0.1"

def call(can_say_hello):
    can_say_hello.say_hello()
```

функция `call` расчитывает на то,
что переданный ей аргумент умеет здороваться.
Иначе говоря, имеет атрибут `"say_hello"`,
который можно вызвать как функцию.

Что ж, оба класса подходят:

```python
anon = Anon()
deanon = Deanon()

call(anon)
call(deanon)
```

## Классы и объекты

Объекты и классы соотносятся так же, как "единица" и "число".

Хотя, в Python, класс = тип.

То есть, `int` — это и класс.

А `1` — объект класса `int`.

Как создать объект? Вызвать класс как функцию:

```python
s = str()
i = int()
u = User()
```

Проверить, что объект является объектом какого-то класса:

```python
isinstance(1, int)
isinstance(True, int)  # любителям type(True) == int обратить внимание!
isinstance("", str)
isinstance(u, User)
```

Классы [создают объекты](https://docs.python.org/3/reference/datamodel.html#object.__init__).

Метаклассы [создают классы](https://docs.python.org/3/reference/datamodel.html#creating-the-class-object).

## Атрибуты объектов, классов и вообще

Класс, когда он создан, присутствует в единственном числе.

Тогда как объектов этого класса можно насоздавать сколько угодно.

Атрибуты класса наследуются всеми его объектами,
и если класс такой атрибут изменит —
это затронет все остальные объекты, которые он породил:

```python
class C:
    attr = 1

print(C.attr)  # 1

objs = [C() for _ in "123"]

for obj in objs:
    print(obj.attr)  # 1

C.attr = "xxx"

for obj in objs:
    print(obj.attr)  # "xxx"
```

А вот объекты могут иметь свои собственные аттрибуты,
и их изменение не повлияет ни на другие объекты, ни на сам класс:

```python
class C:
    attr = 1

x, y = (C(), C())

print(C.attr)  # 1
print(x.attr)  # 1
print(y.attr)  # 1

x.attr = "zzz"

print(C.attr)  # 1
print(x.attr)  # "zzz"
print(y.attr)  # 1
```

Методы — функции, объявленные внутри класса — являются атрибутами класса.

Однако, у них своеобразная сигнатура:

```python
class C:
    def meth(self, a, b):
        return a + b

obj = C()

# в сигнатуре три аргумента, а в вызове - два!
obj.meth(100, 200)  # 300
```

Дело в том, что согласно понятию [инкапсуляции](https://ru.m.wikipedia.org/wiki/%D0%98%D0%BD%D0%BA%D0%B0%D0%BF%D1%81%D1%83%D0%BB%D1%8F%D1%86%D0%B8%D1%8F_(%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5)), метод выполняет действия **над** объектом. А чтобы знать, какой конкретный объект обрабатывать, используется аргумент `self`.

Используя пример выше: вот эти два вызова по сути одно и то же:

```python
# 1
obj.meth(5, 5)  # 10

# 2
C.meth(obj, 5, 5)  # 10
```

В случае "1", аргументов у `meth` два, т.к. первый — `self` — автоматически связывается с `obj`. Метод вызывается как метод, "метод" = "объект" + "функция, которая этот объект получает как аргумент `self`".

В случае "2", аргументов у `meth` три, т.к. он вызывается как функция, а функция — см. `def ...` — требует три аргумента. Поэтому первым приходится явно передавать объект, а потом — все остальные.

## Конструирование

Чтобы управлять созданием объектов, нужно (пере-)определить медод `__init__`. Такой метод называется "конструктор".

Раз это метод, то и сигнатура будет с `(self, ...)`:

Например, сделаем класс `User`, который параметризуется именем и емейлом:

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    # сюда не смотрите!
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, email={self.email!r})"

alice = User("alice", "a@a.com")
bob = User(email="a@a.com", name="Bob")

print(alice)  # User(name='alice', email='a@a.com')
print(bob)  # User(name='Bob', email='a@a.com')
```

Конечно, можно все атрибуты заполнять вручную:

```python
class User:
    # сюда не смотрите!
    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, email={self.email!r})"

alice = User()
alice.name = "alice"
alice.email = "x"

bob = User()
bob.name = "Bob"
bob.email = "x"

print(alice)  # User(name='alice', email='x')
print(bob)  # User(name='Bob', email='x')
```

Но зачем?

К тому же, объекты, хоть и будут относиться к одному и тому же типу `User`,
потенциально могут иметь разные атрибуты, и поэтому всё же являть собой разрозненные сущности:

```python
alice, bob = [User(), User()]

alice.name = "alice"
bob.email = "x"

print(alice)  # AttributeError: no email
print(bob)  # AttributeError: no name
```

## Наследование

Классы можно наследовать друг от друга:
при этом наследник получает все атрибуты родителя в наследство,
плюс может добавлять свои:

```python
class Summator:
    def add(self, a, b):
        return a + b

class Multiplicator(Summator):
    def multiply(self, a, b):
        result = 0
        for _ in range(b):
            result += a
        return result

s = Summator()
m = Multiplicator()

# родитель умеет только складывать
s.add(1, 2)  # 3

# а потомок ещё и научился умножать
m.add(1, 2)  # 3
m.multiply(0, 10)  # 0

# родитель умножать не умеет:
s.multiply(-1, -1)  # AttributeError: no "multiply"
```

## Перегрузка

А что, если потомок захочет родительские алгоритмы делать по-своему?

Потомку придётся переопределить родительский метод. Это называется — "перегрузка":

```python
class IntegralDivisor:
    def divide(self, dividend, divisor):
        quotient = dividend // divisor
        return quotient

class FractionDivisor(IntegralDivisor):
    def divide(self, dividend, divisor):
        quotient = dividend // divisor
        remainder = dividend % divisor
        return (quotient, remainder)

i = IntegralDivisor()
f = FractionDivisor()

i.divide(10, 7)  # 1
f.divide(10, 7)  # (1, 3)
```

Хорошо, но что, если нет нужды, как в примере выше,
*полностью* переопределять наследие родителя?
Иначе говоря, вызвать метод родителя с тем же именем?
Как различить, чей метод?

Вариантов несколько:

1. использовать `super`:

    ```python
    class IntegralDivisor:
        def divide(self, dividend, divisor):
            quotient = dividend // divisor
            return quotient

    class FractionDivisor(IntegralDivisor):
        def divide(self, dividend, divisor):
            # self связывается super-ом автоматически
            quotient = super().divide(dividend, divisor)
            remainder = dividend % divisor
            return (quotient, remainder)
    ```

1. использовать имя родителя:

    ```python
    class IntegralDivisor:
        def divide(self, dividend, divisor):
            quotient = dividend // divisor
            return quotient

    class FractionDivisor(IntegralDivisor):
        def divide(self, dividend, divisor):
            # первый аргумент придётся передавать самому!
            quotient = IntegralDivisor.divide(self, dividend, divisor)
            remainder = dividend % divisor
            return (quotient, remainder)
    ```

Конструктор тоже можно перегружать:

```python
class Profile:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Profile(name={self.name})"


class TelegramProfile(Profile):
    def __init__(self, phone, name):
        Profile.__init__(self, name)
        self.phone = phone

    def __repr__(self):
        p = Profile.__repr__(self)
        return f"Telegram(phone={self.phone}, profile={p})"


class InstagramProfile(Profile):
    def __init__(self, insta, name):
        Profile.__init__(self, name)
        self.insta = f"@{insta}"

    def __repr__(self):
        p = Profile.__repr__(self)
        return f"Instagram(insta={self.insta}, profile={p})"


class User(TelegramProfile, InstagramProfile):
    def __init__(self, name, phone, insta):
        TelegramProfile.__init__(self, phone, name)
        InstagramProfile.__init__(self, insta, name)

    def __repr__(self):
        t = TelegramProfile.__repr__(self)
        i = InstagramProfile.__repr__(self)
        return f"User(telegram={t}, instagram={i})"


u = User("alex", "+1", "abc")

# User(telegram=Telegram(phone=+1, profile=Profile(name=alex)), instagram=Instagram(insta=@abc, profile=Profile(name=alex)))
print(u)
```

## Проблемы наследования и MRO

Проблемы наследования возникают только у тех, кто наследуется от более чем одного родителя.

Пример выше это хорошо иллюстрирует.

А кому нужно больше — для вас есть MRO: [Хабр](https://habr.com/ru/post/62203/)

И ["diamond problem"](https://www.quora.com/What-is-the-diamond-problem-in-programming):

```python
class First: ...
class Second: ...

class A(First, Second): ...
class B(Second, First): ...

class XXX(A, B):
    pass
```

## Специальные методы

- `__init__`
- `__eq__` / `__gte__` / ...
- `__nonzero__`
- `__getitem__`
- [тысячи их](https://docs.python.org/3/reference/datamodel.html#special-method-names)

## Создание классов

Как объекты создают классы — это всем известно.

А как вот так же, на лету, создать сам класс?

Очень просто:

```python
def initialize(obj, name, email):
    obj.name = name
    obj.email = email


def represent(obj):
    classname = obj.__class__.__name__
    name = obj.name
    email = obj.email
    return f"{classname}(name={name!r}, email={email!r})"


C = type(
    # class name
    "User",

    # base classes
    (),

    # dict: то самое "пространство имён"
    {
        "__init__": initialize,
        "__repr__": represent,
    }
)

alice = C(name="alice", email="x")

# User(name='alice', email='x')
print(alice)
```

## Метаклассы

Если вы не знаете, что это — оно вам не надо.

