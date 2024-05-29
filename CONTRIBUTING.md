# Разработчикам StaticJinjaPlus

В этом документе собраны те рекомендации и инструкции, которые необходимы разработчикам StaticJinjaPlus, но бесполезны для прикладных программистов — пользователей StaticJinjaPlus. Если вы пользователь, а не разработчик StaticJinjaPlus — перейдите в [README.md](https://github.com/MrDave/StaticJinjaPlus/blob/main/README.md).

## Оглавление

- [Как развернуть local-окружение](#Как-развернуть-local-окружение)
   - [Хуки pre-commit](#Хуки-pre-commit)
   - [Как запустить линтеры Python](#Как-запустить-линтеры-Python)
   - [Pytest](#Pytest)



## Как развернуть local-окружение

Для разработки ПО и запуска автотестов вам понадобится набор инструментов. Инструкции по их установке ищите на официальных сайтах:

- [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [Install pre-commit hooks manager](https://pre-commit.com/)
- [Install pipx](https://github.com/pypa/pipx?tab=readme-ov-file#install-pipx)
- [Install poetry with pipx](https://python-poetry.org/docs/#installing-with-pipx)

Склонируйте репозиторий. Перейдите в корневой каталог репозитирия.

Создайте виртуальное окружение:

```PowerShell
StaticJinjaPlus$ python3 -m venv ../venv
```

Активируйте виртуальное окружение. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source ../venv/bin/activate`

Установите все зависимости, включая библиотеки для разработки и отладки:

```PowerShell
StaticJinjaPlus$ pip install -r requirements-dev.txt
```


## Хуки pre-commit

В репозитории используются хуки pre-commit, чтобы автоматически запускать линтеры и автотесты. 
В корне репозитория запустите команду для настройки хуков:

```PowerShell
StaticJinjaPlus$ pre-commit install
```

В последующем при коммите автоматически будут запускаться линтеры и автотесты. Есть линтеры будет недовольны, или автотесты сломаются, то коммит прервётся с ошибкой.

<img width="725" alt="image" src="https://github.com/SGKespace/StaticJinjaPlus/assets/55636018/9ce1b85c-fd69-45dd-9846-77c0fc2b3d22">


## Как запустить линтеры Python

Перед запуском линтеров предварительно активируйте виртуальное окружение:

Запустите линтер Flake8:

```PowerShell
StaticJinjaPlus$ flake8
```

Пример результата вывода

<img width="632" alt="image" src="https://github.com/SGKespace/StaticJinjaPlus/assets/55636018/d652d97e-5265-4735-8730-5b9c83f1c24d">

Запуск линтер mypy:

```PowerShell
StaticJinjaPlus$ mypy main.py
Success: no issues found in 1 source file
```


## Pytest

Pytest используется для написания и запуска автотестов.

Запустите автотесты предварительно активировав виртуальное окружение:

```shell
$ pytest
=========================== test session starts ===========================
platform win32 -- Python 3.11.5, pytest-8.1.1, pluggy-1.4.0
collected 2 items
rootdir: C:\Dev\StaticJinjaPlus
test_sample.py .F                         [100%]
================================= FAILURES ========================================
___________________________________ test_wrong_answer ____________________________
    def test_wrong_answer():
>       assert func(10) == 5
E       assert 11 == 5
E        +  where 11 = func(10)

test_sample.py:9: AssertionError

FAILED test_sample.py::test_wrong_answer - assert 11 == 5
=========================== 1 failed, 1 passed in 0.10s ===========================
```
