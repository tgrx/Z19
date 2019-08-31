# Ответы на вопросы

## Примеры визуализации работы с Git в крупных проектах

- [History of Python](https://www.youtube.com/watch?v=cNBtDstOTmA)
- [Linux kernel](https://www.youtube.com/watch?v=P_02QGsHzEQ)

## Программа для работы с Git на iOS

[Working Copy](https://workingcopyapp.com)

## Как переписать историю, соединив несколько коммитов в один (squash)?

`git rebase -i "после-этого-коммита"`

Руководство на [Stack Overflow](https://stackoverflow.com/questions/5189560/squash-my-last-x-commits-together-using-git)

## Как выполнить слияние

- `git merge`
- `git rebase`

Перед применением - изучите, как разрешать конфликты!

План Б:

- `git merge --abort`
- `git rebase --abort`
