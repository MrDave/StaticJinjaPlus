Запуск локально в виртуальном окружении

```
python3 -m venv venv
# Активируйте его. На разных операционных системах это делается разными командами:
# Windows: .\venv\Scripts\activate
# MacOS/Linux: source venv/bin/activate
venv/bin/pip install -U pip setuptools
venv/bin/pip install poetry
cp ./pyproject.toml ./poetry.lock ./venv/bin
flake8  $(pwd)/StaticJinjaPlus
```

Результат

<img width="1020" alt="image" src="https://github.com/SGKespace/StaticJinjaPlus/assets/55636018/a59a5fdc-7b55-4da5-9e09-51ab07375733">
