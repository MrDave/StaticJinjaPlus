```
 docker build . --file Dockerfile --tag linter
```

Пример проверки 
```
 docker run -v "$(pwd)/StaticJinjaPlus:/StaticJinjaPlus" linter flake8 /StaticJinjaPlus
```

<img width="1007" alt="image" src="https://github.com/SGKespace/StaticJinjaPlus/assets/55636018/c7ba3697-c547-48ff-a765-067fd0a3db72">


