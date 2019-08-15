# Конспект

## Консоль

Windows: `cmd.exe` или терминал от Git Scm

Linux/Mac: ваш любимый терминал

### Команды

Пояснение: для каждой операции привожу две команды, первая - для Windows, если работаете в `cmd.exe`. Вторая - для Linux, Mac OS X и терминала Git SCM.

- узнать, в какой папке сейчас находимся:
    - `cd`
    - `pwd`
- перейти в другую папку:
    - `cd путь\к\папке`
    - `cd путь/к/папке`
- создать папку:
    - `mkdir имя`
    - `mkdir имя`

## Python

[Документация](https://docs.python.org/3/index.html)

[Руководство](https://docs.python.org/3/tutorial/index.html)

Версия Python: используй 3.x.

Интерпретаторы:

- [CPython](https://www.python.org/): 3.7.3
- [PyPy](https://pypy.org/): 3.6

Как выполнить код из файла:

```shell script
# Windows
python C:\путь\к\файлу\code.py

# Linux
python путь/к/файлу/code.py
```

## Git

[Официальный сайт Git](https://git-scm.com/)

### Команды

- Клонировать репозиторий:
    - `git clone`
    - Например, учебный: `git clone https://github.com/tgrx/Z19`
        
        Будет создана папка `Z19` в той папке, в которой было выполнено клонирование.

- Посмотреть состояние кэша, имя текущей ветки и пр.:
    -  `git status`

- Посмотреть историю коммитов в текущей ветке:
    - `git log`

- Обновить локальный репозиторий, скачав данные с сервера:
    - `git fetch`

- Скачать саму ветку с сервера:
    - Текущую: `git pull`
    - Конкретную, например, `master`: `git pull origin master`

- Посмотреть список всех веток:
    - `git branch`

- Ответвиться от текущей ветки, создать новую:
    - `git checkout -b "имя ветки"`

- Добавить новые или изменённые файлы в локальный кэш:
    - `git add файл`

- Удалить файл сразу из кэша и вообще:
    - `git rm файл`

- Сохранить изменения, сделав коммит:
    - `git commit`
    - Прокомментировать, что было сделано в этом коммите: `git commit -m "новая версия""`

- Залить свою историю (коммиты) в ветку на сервере:
    - Текущую ветку: `git push`
    - Конкретную ветку, например, `master`: `git push origin master`


### Пример работы с Git

Допустим, нужно создать ["hello world"](https://ru.wikipedia.org/wiki/Hello,_world!).
На компе установлен Python и Git. Опционально, PyCharm или другая среда разработки.

1. Клонируем этот репозиторий себе на комп
1. Открываем проект
    1. Консоль: переходим в папку `Z19`
    1. PyCharm: открываем проект, указывая в качестве папки проекта папку `Z19`
1. Синхронизируемся с сервером:
    1. консоль: `git fetch`
    1. PyCharm: VCS > Update project
1. Создаём свою ветку (пример имени: `alexander-lesson-01`):
    1. Консоль: `git checkout -b alexander-lesson-01`
    1. PyCharm: VCS > Git > Branches > New branch
1. Создаём папку со своим именем (логин из Github, имя-фамилия, никнейм из Телеграмма - лишь бы уникальное, малленькими латинскими буквами с подчёркиваниями вместо пробелов) внутри `Z19/homeworks`:
    1. Консоль:
        1. `cd homeworks`
        1. `mkdir alexander`
    1. PyCharm: правый клик по `Z19/homeworks` > New > Directory
1. Создаём модуль Python, где будем писать код:
    1. Консоль:
        - Windows: `notepad Z19\homeworks\alexander\lesson01.py`
        - Остальные: `vim Z19/homeworks/alexander/lesson01.py`
    1. PyCharm: правый клик по `Z19/homeworks/alexander` > New > Python file > "lesson01.py"
1. Пишем код!
1. Добавляем файл в Git:
    1. Консоль: `git add Z19/homeworks/alexander/lesson01.py`
    1. PyCharm: правый клик по файлу > Git > Add
1. Фиксируем изменения, создаём коммит:
    1. Консоль: `git commit -m "lesson 1"`
    1. PyCharm: VCS > Commit
1. Отправляем ветку на сервер:
    1. Консоль: `git push origin alexander-lesson-01`
    1. PyCharm: VCS > Git > Push
1. Заходим в GitHub, находим [там](https://github.com/tgrx/Z19/branches) свою ветку, жмём "New pull request"
    - Выбираем base: `master`
    - Пишем, что именно сделали
    - Жмём "Create pull request"
