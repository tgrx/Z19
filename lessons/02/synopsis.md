# Конспект

## Git

### Основы

Назначение — управление историей при совместной работе.

История — совокупность коммитов и связей между ними.

Коммит — элемент всей системы, зафиксированное состояние репозитория.

Репозиторий — место, где хранятся файлы проекта
- локально:
    папка с папкой `.git` внутри,
    создаётся автоматически
    при клонировании или инициализации репозитория
- удалённо: на сервере (GitHub)

Удалённый репозиторий в контексте локальной работы ещё может называться:
- origin
- upstream
- remote

Pull request (Merge request) - запрос к Git на слияние одной ветки (base) с другой.

### Процесс

<details><summary>**NB**</summary>

В описании процесса использую название
_"base-branch"_ в качестве базовой ветки, это:
- `master`, если делаете новое задание;
- ваша рабочая ветка, если создаёте новую от неё;

и название _"new-branch"_ в качестве новой ветки, это:
- ваша рабочая ветка, если ответвлялись от `master`;
- ваша новая ветка, если ответвлялись от _"base-branch"_;

Если по шагам выполняете действия,
то эти названия надо заменить на свои.

Если сомневаетесь — обязательно переспросите у меня в ТГ.
</details> 

В ходе курса - и, в большинстве проектов -
процесс работы с Git, или flow, будет следующим:

1. Загружаем проект:
    - Терминал: заходим в папку с проектом (Z19)
    - PyCharm: открываем проект, папку с проектом
1. Обновляем локальный репозиторий:
    - Терминал: `git fetch`
    - PyCharm: `VCS > Update project`
1. Выбираем базовую ветку:
    - Терминал: `git checkout base-branch`
    - PyCharm: `VCS > Branches`
        - локальная: `Checkout`
        - с сервера: `Checkout As...` и сохраняем то же имя ветки
1. Синхронизируем базовую ветку:
    - Терминал: `git pull`
    - PyCharm: `VCS > Git > Pull... > "base-branch" > Pull`
1. Переключаемся в новую рабочую ветку:
    - Если надо, создаём новую:
        - Терминал: `git checkout -b new-branch`
        - PyCharm: `VCS > Git > Branches > +New Branch > "new-branch"`
    - Если ветка уже существует:
        1. делаем её рабочей веткой:
            - Терминал: `git checkout new-branch`
            - PyCharm: `VCS > Branches > "new-branch"`
                - локальная: `Checkout`
                - с сервера: `Checkout As...`, имя не меняем
        1. обновляем её:
            - Терминал:
                1. `git pull origin new-branch`
                1. `git merge base-branch`
                1. Подтверждаем "merge commit", если нет конфликта
            - PyCharm:
                1. `VCS > Git > Pull... > "new-branch" > Pull`
                1. `VCS > Git > Merge Changes...`
                    - "Current branch": должна быть _"new-branch"_
                    - "Branches to merge": выбираем _"base-branch"_
                1. Подтверждаем "merge commit", если нет конфликта
    - Дополнительно: смотрим список веток
        - Терминал:
            - только локальные: `git branch`
            - все: `git branch -a`
        - PyCharm: `VCS > Git > Branches` или в правом нижнем углу
1. Работаем в своей ветке, делаем в ней всё, что вам нужно
    1. Всё, что нужно, всё, что вы хотите - переписывайте историю как хотите
        1. но только в пределах своей ветки! в которой работаете только Вы!
1. Фиксируем свою работу - делаем коммит или коммиты
1. Синхронизируем свою ветку с базовой:
    - Терминал:
        1. `git checkout base-branch`
        1. `git pull origin base-branch`
        1. `git checkout new-branch`
        1. `git merge base-branch`
        1. Подтверждаем "merge commit", если нет конфликта
    - PyCharm:
        1. `VCS > Git > Merge Changes...`
            - "Current branch": должна быть _"new-branch"_
            - "Branches to merge": выбираем _"remotes/origin/base-branch"_
        1. Подтверждаем "merge commit", если нет конфликта
1. Заливаем ветку в origin:
    - Терминал: `git push origin new-branch`
    - PyCharm: `VCS > Git > Push... > Push`
1. Создаём пулл-реквест
    1. заходим в Github
    1. жмём кнопку "New pull request"
    1. выбираем в качестве "base" ветку, **от которой создали рабочую**: `base-branch`
    1. выбираем в качестве "compare" свою рабочую ветку: `new-branch`
    1. подтверждаем
1. Пьём кофе, отдыхаем, работа выполнена

Обучающие видосы:

- [раз: типичный процесс, 3 минуты](https://www.youtube.com/watch?v=e8PGuOyZ3YU)
- [два: про ветки, 6 минут](https://www.youtube.com/watch?v=Ao1beK2rEIY)
- [три: целый плейлист](https://www.youtube.com/watch?v=M-O8ZNW9icQ&list=PLyCj4RCToz5BEcpZgwLfAhzxVRlDY3z-O)
- [четыре: плейлист на русском](https://www.youtube.com/playlist?list=PLDyvV36pndZHkDRik6kKF6gSb0N0W995h)

Пример: [организация работы с Git в Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) - там вообще своё собственное решение, но кто интересуется, можно проанализировать идеи.

## Ресурсы

Видео: [What is Git?](https://git-scm.com/video/what-is-version-control)

Ещё видео: [тысячи их](https://git-scm.com/videos)

Шпаргалка по командам (на английском): [PDF](https://github.github.com/training-kit/downloads/github-git-cheat-sheet.pdf)

