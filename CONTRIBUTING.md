<!-- omit in toc -->
# Разработчикам StaticJinjaPlus

В этом документе собраны те рекомендации и инструкции, которые необходимы разработчикам StaticJinjaPlus, но бесполезны для прикладных программистов — пользователей StaticJinjaPlus, Вам интересен [README.md](https://github.com/MrDave/StaticJinjaPlus/blob/main/README.md).


<!-- omit in toc -->
## Оглавление

- [Как запустить линтеры Python](#Как-запустить-линтеры-Python)
- [I Have a Question](#i-have-a-question)
- [Задел на будущее](#Задел-на-будущее)
 


## Как запустить линтеры Python
  Запуск локально в обязательно в отдельном виртуальном окружении

```
  python3 -m venv venv
```
  
Активируйте его. На разных операционных системах это делается разными командами:
Windows: .\venv\Scripts\activate
MacOS/Linux: source venv/bin/activate

Запустите проверку:
```
venv/bin/pip install -U pip setuptools
venv/bin/pip install poetry
cp ./pyproject.toml ./poetry.lock ./venv/bin
flake8  $(pwd)/StaticJinjaPlus
```



## I Have a Question
  Задел на будущее




## Задел на будущее
  Задел на будущее



This project and everyone participating in it is governed by the
[StaticJinjaPlus Code of Conduct](https://github.com/SGKespace/StaticJinjaPlusblob/master/CODE_OF_CONDUCT.md).
By participating, you are expected to uphold this code. Please report unacceptable behavior
to <sgkond@gmail.com>.
  
