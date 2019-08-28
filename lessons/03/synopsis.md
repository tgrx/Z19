# Типы данных 101

## Определения

### Официальная метафизика

_"Data type - an attribute of data
which tells the compiler or interpreter
how the programmer intends to use the data."_ - [en:wiki](https://en.wikipedia.org/wiki/Data_type)

_"Тип — множество значений и операций на этих значениях."_ - [ru:wiki](https://ru.wikipedia.org/wiki/%D0%A2%D0%B8%D0%BF_%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)

### Диванная метафизика

Тип – атрибут данных, который показывает, что можно с этими данными делать.

Тип — абстракция, обобщение элементов.

Понятия "тип" и понятие "объект" соотносятся как:
- клавиатуры компов в аудитории и понятие "клавиатура"
- компы в аудитории и понятие "компьютер"

Введём операцию `type: t => T`, которая будет каждой сущности `t` вычислять её тип `T`.
- `type(ваш домашний комп) == компьютер`
- `type(вы в контексте этого курса) == студент`

Применительно к данным:
- `type(коллекция букв и символов) == строка`
- `type(100500_000_000) == целое число`
- `type(0.5) == число с плавающей точкой`

Тип – это элемент множества типов (\o ZFC).

`type` переводит множество объектов в множество типов.

Пример: определим "множество" элементов и напечатаем для каждого элемента его тип:

```python
elements = (
    True,
    1,
    1.,
    1j,
    "kek",
    b"lol",
    1/3,
    Decimal("0.33"),
    [],
    (),
    {},
    None,
    object,
    type,
    type("Wow", (), {}),
)

for element in elements:
    print(f"{element!r:<25}\t=>\t{type(element).__name__:<10}")
```

Результат:

```
True                     	=>	bool
1                        	=>	int
1.0                      	=>	float
1j                       	=>	complex
'kek'                    	=>	str
b'lol'                   	=>	bytes
0.3333333333333333       	=>	float
Decimal('0.33')          	=>	Decimal
[]                       	=>	list
()                       	=>	tuple
{}                       	=>	dict
None                     	=>	NoneType
<class 'object'>         	=>	type
<class 'type'>           	=>	type
<class '__main__.Wow'>   	=>	type
```

Построим множество типов:

```python
types = {type(element) for element in elements}
```

Вот оно:
```
{
    NoneType,
    bool,
    bytes,
    complex,
    decimal.Decimal,
    dict,
    float,
    int,
    list,
    str,
    tuple,
    type,
}
```

Конечно, реальное множество типов больше, чем в этом примере.

Типы образуют иерархию: чем абстрактнее тип, тем он выше в иерархии.

Например, Макбук и [IBM Summit](https://en.wikipedia.org/wiki/Summit_&#40;supercomputer&#41;) относятся к типу "компьютер",
но первый можно перенести руками, а второй - нет.

Тогда можно определить такой тип, как "переносимый компьютер", который означает, что элементы данного типа можно как носить в руках, так и выполнять какие-то вычисления.

Тогда, тип "компьютер" будет стоять выше в иерархии, чем "переносимый компьютер", т.к. он объединяет большее количество элементов и имеет меньше характеристик: `{можно выполнять вычисления}` vs. `{можно выполнять вычисления, можно носить}`.

Самый общий, самый абстрактный тип - это "тип". Кто не верит — почитайте официальные определения, они настолько размыты, что под них попадает практически всё мыслимое, а в списке характеристик типа "тип" присутствует, наверное, только что-то типа `{характеризует что-то другое}`.

## Типы данных в Python

### Модель

Данные определённого типа находятся где-то в памяти.

Узнать, где: `id(x)`. Например: `id(1)`. Или `id("abc")`.

Переменная — это "имя" для данных в памяти.

Одни и те же данные можно по-разному назвать: несколько переменных могут указывать на одни и те же данные.

Пример:

```python
x = y = 1
id(x) == id(y)  # True
x is y  # True 
```

Сравнение результатов `id()` — это то же самое, что и оператор `is`.

Короткие строки, числа до 100 (около того) уже хранятся в памяти, поэтому id всегда одинаково:

```python
x = 4 // 2
y = 2 // 1
x is y  # True
```

Если объект большой и его ещё в памяти нет, но мы его создаём и тут же именуем двумя и более переменными — они все будут ссылаться на него и id для всех переменных будет одинаковое:

```python
x = y = z = 100 ** 200  # очень большое число!
id(x) == id(y) == id(z)  # True
```

Однако, стоит повторить пример выше с делением 4, 2, 1 — только заменив на большую степень — как сразу id станут разными:

```python
x = 100 ** 200
y = 100 ** 200

x is y  # False!

# а сами данные одинаковые:
x == y  # True
```

Чтобы удалить связь переменной с данными, используется команда `del`:

```python
x = [100 ** 500]
y = {"x": x, "z": 14 ** 88}

del x
# и теперь на [100 ** 500] указывает только y["x"]

del y["z"]
# и теперь на 14 ** 88 не указывает никто, а в y остался только "x"

del y
# и теперь никто не указывает ни на что

# а теперь приходит garbage collector и убирает за всеми
```

Если данные можно изменить, то такой тип называется _изменяемым_, или _мутабельным_.
Если данные изменить нельзя, то такой тип называется _неизменяемым_ или _иммутабельным_.

Пример изменяемого типа:

```python
x = y = [1]
x is y  # True

x += [2]  # список был [1], а стал [1, 2]
x is y  # True: обе переменных указывают на один список: [1,2]
```

А вот пример неизменяемого:

```python
x = y = (1,)
x is y  # True

x += (2,)  # вроде мы добавляем элемент в тот же кортеж, но...
x is y  # False!
print(x)  # (1, 2) - создан новый кортеж!
print(y)  # (1,) - а `y` указывает на старый

y += (2,)  # поправим ситуацию?
x is y  # False: нет
x == y  # True: сами данные равны
```

### Создание объектов

Объекты - экзепляры типа - можно создавать двумя способами.

Первый — написать само значение — это называется "литерал":

```python
10  # int
"abc"  # str
b"k\x31k"  # bytes
{1, 2}  # set
[3, 4]  # list
(5,)  # tuple
{1:100, 2:200}  # dict
True  # bool, уже создан до нас
False  # bool, уже создан до нас
None  # NoneType, уже создан до нас
...  # Ellipsis, уже создан до нас
```

Второй - вызвать тип как функцию, и передать функции что-нибудь, из чего можно построить объект этого типа:

```python
int("10")  # число из строки
int(10)  # число из числа
float(5)  # число вещественное из числа целого
complex(1, 2)  # (1+2j)
str(10)  # "10" - строка из числа
list(str(10))  # ["1", "0"]  - список из строки
list((1,))  # [1] - список из кортежа
bool(2)  # True
```

Если объект не удастся создать, будет ошибка `ValueError`:

```python
int("kek")  # ValueError: invalid literal for int() with base 10: 'kek'
```

Или `TypeError`:

```python
set(5)  # TypeError: 'int' object is not iterable
```

### Встроенные типы

#### NoneType

Существует единственный объект этого типа: `None`. Означает **ничто**.

Используется, когда надо создать переменную, которая неизвестно пока, на что указывает.
Приходится указывать на `None`. Или функция, которая ничего не возвращает: приходится возвращать `None`:

```python
x = None

def f1(): pass

def f2(): return

def f3(): return None

x == f1() == f2() == f3() == None  # True
```

Оператор сравнения `==` работает с `None`, но рекомендуется для такой проверки использовать оператор `is`. Или `is not`:

```python
x = None
y = 0

x is None  # True
y is not None  # True  
```

#### Числа

Числа бывают:
1. Целые: `int`
1. Вещественные: `float`
1. Десятичные: `decimal.Decimal`
1. Комплексные: `complex`

Числа можно складывать, умножать, делить (не на ноль), возводить в степень (`2 ** 1j`), и вообще применять кучу функций из модулей `math` и `cmath`:

```python
import cmath
print(cmath.asin(2))
# sin(1.57 + 1.31j) ~= 2
# А говорили, синус больше единицы не бывает
```

Маленькие целые числа можно сравнивать и используя `is`, но крайне не рекомендуется: поведение неопределённое.

Числа сравниваются операторами `==`, `!=`, `>=`, `<=`, `>`, `<`.

Операторы можно объединять в интервал: `1 < x < 10`.

Вещественные числа тоже можно сравнивать, но могут быть глюки:

```python
10.0 == ( (10.0 / 77) * 77)  # False! но может и повезёт
```

С `Decimal` такой проблемы нет:

```python
from decimal import Decimal as D

x = D("10.0")
y = D(77.0)

x == ( (x / 77) * 77 )  # True
x == ( (x / y) * y )  # True
```

Зато `Decimal` медленнее, чем `float`:

```python
from decimal import Decimal as D
af = 10.0
bf = 77.0

ad = D(af)
bd = D(bf)

%timeit (af / bf) * af  #  ~95 нс
%timeit (ad / bd) * ad  # ~371 нс
```

#### Булевый тип

Представляет собой два логических значения: `True` ("истинно") и `False` ("ложно").

Является продолжением типа `int`. Поэтому:

```python
True == 1  # True
False == 0  # True
True == 2  # False
False == []  # False
True == True  # True
False == False  # True
```

Объекты `True` и `False` существуют сразу при старте Python, и вторых таких создать невозможно.
Поэтому рекомендуется для сравнения на истинность/ложность использовать оператор `is`:
- бро: `x is True`
- не бро: `x == True`

Конкретно, `1 == True` истинно, а `1 is True` — ложно.

Эти значения можно сравнивать ...но зачем?

```python
False < True
True >= False
```

"Истинными" считаются любые ненулевые значения, а "ложными" — нулевые:

```python
if 88 and "0" and True:
    print(14)  # напечатает

if [] or None or {} or 0 or "" or set() or False:
    print("")  # не напечатает
```

Вычисления `and` и `or` "ленивые":
- если в цепочке `... and ...` появится `False` — то общий результат `False` и дальнейшие предикаты не вычисляются
- если в цепочке `... or ...` появится `True` — то общий результат `True` и дальнейшие предикаты не вычисляются

Если нужно, чтобы все предикаты вычислялись, используются функции-кванторы `all()` и `any()`:

```python
# сколько скобок? почему?
if all((88, "0", True)):
    print(14)  # напечатает

# сколько скобок? почему?
if any(([], None, {}, 0, "", set(), False)):
    print("")  # не напечатает
```

#### Коллекции

Коллекции — это хранилища для других объектов любых типов (грубо).

Неизменяемые: `str`, `tuple`, `frozenset`

Изменяемые: `list`, `set`, `dict`

Коллекции можно передавать друг другу, чтобы создавать одни из других:

```python
tuple("abc")  # ("a", "b", "c")
list({7, 1, 7, 2, 8, 5})  # [1, 2, 5, 7, 8]
```

Строки — особый случай:

```python
set("ab")  # {"a", "b"} - множество
str({"a", "b"})  # "{'a', 'b'}" - текстовое представление, а не
```

Коллекции умеют говорить, содержится ли в них какой-то элемент:

```python
1 in [3, 2, 1]  # True
100 in {1: 100}  # False: dict ищет ключ
```

Строки — снова особый случай:

```python
"ab" in ["a", "c", "a", "b"]  # False
"ab" in "acab"  # True
```

Можно достать конкретный элемент:
- списки, кортежи, строки - по позиции: `"abc"[1]` или `(1,2,3,4)[1:3]`
- словари: по ключу: `{True: False}[1]`
- множества: не умеют
    - или такое: `next(iter({7,1,2,8,5}))` - первый попавшийся
    - или только для `set`: `x.pop()`

Можно делать срезы:
- списки, кортежи, строки: `x[1:]` или `x[:-5]` или `x[1:3]`
- множества, словари: нельзя

Можно обращать порядок:
- списки, кортежи, строки: `x[::-1]` или `tuple(reversed(x))` или `list(reversed(x))`
- списки: на месте:

    ```python
    x = [3, 2, 1]
    y = list(reversed(x))
    z = x[::-1]
    x.reverse()  # новый список не создаётся
  
    x == y == z  # True
    ```
    
- множества, словари: нельзя

Можно сортировать:
- кортежи, строки, фроузенсеты - с созданием нового списка: `sorted((3,2,1))`
- списки - и как кортежи, и на месте (in place):

    ```python
    x = [3, 2, 1]
    y = sorted(x)
    x.sort()  # новый список не создаётся
  
    x == y  # True
    ```

- дикты: создаётся список с ключами: `sorted({3:1, 2:4})`

Можно сделать копию:
- кортежи, строки, списки: `x[:]`
- списки, множества, словари: `x.copy()`

##### Строки

Упорядоченная последовательность строк.
Да, строка состоит из строк.
Элемент строки - строка.

Литерал: `"123"`

Тип: `str(123)`

Можно соединять (конкатенировать): `"abc" + "cde"`

Можно соединять разделителем: `" ".join("0123456789")`

Можно форматировать:
- рухлядь: `"%d %s" % (1, "a")`
- понты: `"{} {}".format(1, "a")`
- более-менее: `"{1} {0}".format(1, "a")`
- хорошо: `"{y} {x} {y}".format(x=1, y="a")`
- топчик:

    ```python
    from cmath import e, pi
    
    i = 1j
    
    print(
        f"e ** (i pi) + 1 = {e ** (i * pi) + 1}"
    )
    ```

Можно кодировать в байты: `"кек".encode()`

И обратно: `"кек".encode().decode()`

Если строка очень длинная, то можно разделить её на части:

```python
s = (
    "100"  # нет запятой!
    "000"  # нет запятой!
    "000"  # нет запятой!
)
```

А если надо сохранить большой текст, как есть, со всеми отступами - то используются тройные кавычки `"""`:

```python
s = """
тут
     пишем
          как
   захотим
и
даже
переходы
на новую строку
    сохранятся
 ))
"""
```

f-строки тоже работают (и форматирование и всё остальное):

```python
from cmath import e, pi

i = 1j

x = e ** (i*pi) + 1

# зацените отступ в строке с "Euler identity"!
print(f"""

Euler identity:

    e ** (i pi) + 1 = 0

    e  = {e:.2f}
    i  = {i:.2f}
    pi = {pi:.2f}

    Python result: {x.real:.2f}{"-" if x.imag < 0 else "+"}{x.imag:.2f}  

""")
```

Можно сравнивать: `"abc" < "af"`

Можно размножать: `"a" * 100`

Можно посчитать: `"acab".count("a")`

Можно найти позицию элемента: `"acab".index("b")`

Можно капитализировать: `"acab".capitalize()`

Или, если мало: `"acab".upper()`

Можно проверить, что содержимое - число: `"10".isdigit()`

Да и вообще [много всего](https://docs.python.org/3/library/stdtypes.html#str)! 

##### Кортежи

Упорядоченная последовательность каких-либо элементов. 

Литерал: `(1,)` / `1,` / `(1,2,3)`

Тип: `tuple([1,2,3])`

Можно соединять в один: `(1,2) + (2,3)`

Можно сравнивать: `(1,1000) < (0, 1)`

Можно размножать: `(1,) * 100`

Можно посчитать: `(1,1,1).count(1)`

Можно найти позицию элемента: `(3,2,1).index(2)`

##### Списки

Упорядоченная последовательность каких-либо элементов.

Литерал: `[1]`

Тип: `list((1,))`

Можно соединять в один: `[1] + ["2"]`

Можно сравнивать: `[2] > [1, 1, 1]`

Можно размножать: `["a"] * 100`

Можно посчитать: `[1, 1, 1].count(1)`

Можно найти позицию элемента: `[3, 2, 1].index(2)`

Можно удалить элемент в позиции:

```python
x = list("abc")
del x[1]
```

Можно выдернуть первый элемент: `x.pop()`

А можно добавлять элемент в конец:

```python
x = list("aca")
x.append("b")
# или
x += ["b"]
```

А можно и сразу пачкой: `x.extend([1,2,3])`

Можно удалить определённый элемент - первый попавшийся:

```python
x = list("acabb")
x.remove("b")
```

Можно вообще психануть и всё удалить:

```python
x = [1, 2, 3]
x.clear()
del x[:]  # или даже так!
```

Да и вообще [много всего](https://docs.python.org/3/library/stdtypes.html#list)!

##### Множества

Множество не сохраняет порядок элементов.
Множество содержит только уникальные элементы.
Во множество можно добавлять элементы только неизменяемых типов (или хешируемых).

Поиск элементов во множестве очень быстрый. 

Литерал: `{"",}`

Тип: `set("")`

Можно объединять: `{1, 2} | {2, 3}`

Можно разъединять: `{1, 2} ^ {2, 3}`

Можно вычитать: `{1, 2} - {2, 3}`

Можно проверять пересечение: `{1, 2} & {2, 3}`

Можно сравнивать, но нельзя: `{1,} < {2,}`

Можно проверить подмножество: `{1, 2}.issubset({1, 2, 3})`

Можно проверить надмножество: `{1, 2, 3}.issuperset({1, 2})`

Пустое множество является подмножеством для любого другого (\o ZFC): `set().issubset({1, 2})`

Можно добавить элемент: `x.add(1)` (но не во frozenset)

Можно удалить элемент: `x.remove(1)` - но если такого уже и нет, будет ошибка!
Для безопасного удаления используется `x.discard(1)` 

Можно удалить всё: `x.clear()`

##### Словари

Это самый лучший и самый любимый всеми тип данных в Python.

Смысл: отображение ключей на значения.

Ключами могут быть только объекты неизменяемых типов: числа, строки, кортежи, фроузенсеты.
Или свой личный тип - если он будет хешируемым.

Поиск значения по ключу очень быстрый.

Литерал: `{1: 100, 2: 200}`
Тип:
    1. `dict([(1, 100), (2, 200)])`
    2. `dict(a=1, b=2)`

Можно получить значение по ключу: `{True: "yeah"}[1]`.
Если ключа нет - будет ошибка `KeyError`.

Чтобы безопасно достать или значение или `None`: `{}.get("key")`.

Чтобы достать или значение, или подставить какую-то замену: `{}.get("key", "default value")`

Можно достать значение, если оно есть, а если нет, создать и достать:

```python
x = {"d": []}
x["d"].append(1)  # всё хорошо

x["a"].append(1)
# KeyError: нет ключа "a"

x.get("a").append(1)
# AttributeError: .get("a") вернёт None,
# а у None нет аттрибута "append"

x.get("a", []).append(1)
# .get в этом случае вернёт список, конечно, но на него никто не ссылается
# поэтому в этот безымянный список будет добавлена единица,
# затем придёт garbage collector и поделит его на ноль,
# а сам x по-прежнему будет без ключа "а"

x.setdefault("a", []).append(1)
# а вот тут всё сработает: x == {"d": [1], "a": [1]}

x.setdefault("a", []).append(2)
# и тут всё сработает: x == {"d": [1], "a": [1, 2]}
```

Вообще, для подобной логики чаще используют [defaultdict](https://docs.python.org/3.7/library/collections.html#collections.defaultdict).

Можно создать или обновить значение: `x["key"] = "value"`

Можно сразу оптом: `x.update({"a": 1, "b": 2})` 

И ещё [много чего](https://docs.python.org/3/library/stdtypes.html#dict)!