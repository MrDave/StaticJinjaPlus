

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