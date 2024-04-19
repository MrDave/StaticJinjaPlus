# Разработчикам StaticJinjaPlus

В этом документе собраны те рекомендации и инструкции, которые необходимы разработчикам StaticJinjaPlus, но бесполезны для прикладных программистов — пользователей StaticJinjaPlus. Если вы пользователь, а не разработчик StaticJinjaPlus — перейдите в [README.md](https://github.com/MrDave/StaticJinjaPlus/blob/main/README.md).

## Оглавление

- [Как развернуть local-окружение](#Как-развернуть-local-окружение)
- [Как запустить линтеры Python](#Как-запустить-линтеры-Python)
- [Testing](#Testing)


## Как развернуть local-окружение

Для запуска ПО вам понадобятся консольный Git.

Склонируйте репозиторий.

В репозитории используются хуки pre-commit, чтобы автоматически запускать линтеры и автотесты. Перед началом разработки установите [pre-commit package manager](https://pre-commit.com).
В корне репозитория запустите команду для настройки хуков:

```PowerShell
StaticJinjaPlus$ pre-commit install
```

В последующем при коммите автоматически будут запускаться линтеры и автотесты. Есть линтеры будет недовольны, или автотесты сломаются, то коммит прервётся с ошибкой.

<img width="725" alt="image" src="https://github.com/SGKespace/StaticJinjaPlus/assets/55636018/9ce1b85c-fd69-45dd-9846-77c0fc2b3d22">



## Как запустить линтеры Python
Запуск локально обязательно в отдельном виртуальном окружении вне скачанного репозитория

```shell
StaticJinjaPlus$ python3 -m venv ../venv
```
  
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`

Запустите проверку:

```PowerShell
StaticJinjaPlus$ ../venv/bin/pip install -U pip setuptools
StaticJinjaPlus$ ../venv/bin/pip install poetry
StaticJinjaPlus$ cp ./.linters/pyproject.toml ./.linters/poetry.lock ../venv/bin
StaticJinjaPlus$  ../venv/bin/poetry install --no-ansi --directory=../venv/bin
Creating virtualenv py-linters-iyfZ0h-u-py3.12 in /Users/sgk/Library/Caches/pypoetry/virtualenvs
StaticJinjaPlus$ /Users/sgk/Library/Caches/pypoetry/virtualenvs/py-linters-iyfZ0h-u-py3.12/bin/flake8 ../StaticJinjaPlus
```
Пример результаата вывода
<img width="632" alt="image" src="https://github.com/SGKespace/StaticJinjaPlus/assets/55636018/d652d97e-5265-4735-8730-5b9c83f1c24d">


## Testing

The StaticJinjaPlus has 2 tests(collected 2). First show proper work with program, second fails. To run them use `pytest`

```PowerShell
pip install -U pytest
```

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
