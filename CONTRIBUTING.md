# Разработчикам StaticJinjaPlus

В этом документе собраны те рекомендации и инструкции, которые необходимы разработчикам StaticJinjaPlus, но бесполезны для прикладных программистов — пользователей StaticJinjaPlus. Если вы пользователь, а не разработчик StaticJinjaPlus — перейдите в [README.md](https://github.com/MrDave/StaticJinjaPlus/blob/main/README.md).

## Оглавление

- [Как запустить линтеры Python](#Как-запустить-линтеры-Python)


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
cp ./.linters/pyproject.toml ./.linters/poetry.lock ./venv/bin
flake8  $(pwd)/StaticJinjaPlus
```
