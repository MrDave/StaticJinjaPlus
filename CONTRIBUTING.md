# Разработчикам StaticJinjaPlus

В этом документе собраны те рекомендации и инструкции, которые необходимы разработчикам StaticJinjaPlus, но бесполезны для прикладных программистов — пользователей StaticJinjaPlus. Если вы пользователь, а не разработчик StaticJinjaPlus — перейдите в [README.md](https://github.com/MrDave/StaticJinjaPlus/blob/main/README.md).

## Оглавление

- [Как развернуть local-окружение](#Как-развернуть-local-окружение)
- [Как запустить линтеры Python](#Как-запустить-линтеры-Python)


## Как развернуть local-окружение

  Для запуска ПО вам понадобятся консольный Git.
  Склонируйте репозиторий.
  В репозитории используются хуки pre-commit, чтобы автоматически запускать линтеры и автотесты. Перед началом разработки установите [pre-commit package manager](https://pre-commit.com).
  В корне репозитория запустите команду для настройки хуков:

```
pre-commit install
```

  В последующем при коммите автоматически будут запускаться линтеры и автотесты. Есть линтеры будет недовольны, или автотесты сломаются, то коммит прервётся с ошибкой.

<img width="725" alt="image" src="https://github.com/SGKespace/StaticJinjaPlus/assets/55636018/9ce1b85c-fd69-45dd-9846-77c0fc2b3d22">



## Как запустить линтеры Python
  Запуск локально обязательно в отдельном виртуальном окружении

```
python3 -m venv venv
```
  
Активируйте его. На разных операционных системах это делается разными командами:

- Windows: `.\venv\Scripts\activate`
- MacOS/Linux: `source venv/bin/activate`

Запустите проверку:
```
venv/bin/pip install -U pip setuptools
venv/bin/pip install poetry
cp ./StaticJinjaPlus/.linters/pyproject.toml ./StaticJinjaPlus/.linters/poetry.lock ./venv/bin
venv/bin/poetry install --no-ansi
venv/bin/flake8  $(pwd)/StaticJinjaPlus
```
Пример результаата вывода
<img width="632" alt="image" src="https://github.com/SGKespace/StaticJinjaPlus/assets/55636018/d652d97e-5265-4735-8730-5b9c83f1c24d">


