# StaticJinjaPlus

StaticJinjaPlus is a tool to build static sites using [Jinja](https://jinja.palletsprojects.com/).

# Content

- [How to install](#How-to-install)
- [Building sites](#Building-sites)
  - [Watching for changes](#Watching-for-changes)
  - [Specifying templates or build paths](#Specifying-templates-or-build-paths)
  - [Using assets](#Using-assets)
  - [Using context](#Using-context)
  - [Как использовать extends и include](#Как-использовать-extends-и-include)
- [Example templates](#Example-templates)

## How to install

Python should already be installed. This project requires Python3.7 or newer.

Clone the repo / download code.

Using virtual environment [virtualenv/venv](https://docs.python.org/3/library/venv.html) is recommended for project isolation.

Install requirements:
```commandline
pip install -r requirements.txt
```

To check that everything installed correctly try running the script with `--help` flag:
```commandline
python main.py --help
```
Output:
```
usage: main.py [-h] [-w] [--srcpath SRCPATH] [--outpath OUTPATH]

Render HTML pages from Jinja2 templates

options:
  -h, --help         show this help message and exit
  -w, --watch        Render the site, and re-render on changes to <srcpath>
  --srcpath SRCPATH  The directory to look in for templates (defaults to './templates)'
  --outpath OUTPATH  The directory to place rendered files in (defaults to './build')
```
Now you're all ready to build your static sites!


## Building sites

Note: see [Example templates](#example-templates) section for an example with sample templates. Rename the /templates_example folder to /templates to run test templates.

To render html pages from templates, run:
```commandline
python main.py
```
This will look in `./templates` for templates (files whose name does not start with `.` or `_`) and build them to `./build`.

You'll see a message about each template in the output:
```
Rendering index.html...
```

### Watching for changes
To watch for changes in the templates and recompile build files if changes happen, use `-w` or `--watch` argument.
```commandline
python main.py -w

Rendering index.html...
Watching '/home/mrdave/Python Projects/StaticJinjaPlus/templates' for changes...
Press Ctrl+C to stop.
```

### Specifying templates or build paths

To change the source and/or output paths use optional arguments:  
- `--srcpath` - the directory to look in for templates (defaults to `./templates`)  
- `--outpath` - the directory to place rendered files in (defaults to `.`)

Example:
```commandline
python main.py --srcpath other_template_folder --outpath ./built/site

Rendering index.html...
```

### Using assets

To use assets such as `.css` and `.js` files with your templates, place them in `assets` folder inside source path (so `./templates/assets` by default).
In this case StaticJinjaPlus will copy the assets to output folder keeping the same relative paths.

Building log will also include "rendering" the assets:

```commandline
python main.py

Rendering assets/style.css...
Rendering index.html...
```

### Using context
It is possible to pass context for use in your templates by setting environmental variables named as you use them in the templates with the `"SJP_"` prefix.

As an example, if your template includes `thing` variable, pass the `SJP_THING` env variable before building.

```html
<!-- html template -->
<div class="container">
    <h1>Welcome to our website!</h1>
    <p>This is the homepage content. Replace it with your own.</p>
    <p>The thing from context is {{ thing }}</p>
</div>
```
```shell
export SJP_THING="my_thing"
python main.py
```
![](https://imgur.com/TEf3yJ6.png)


## Как использовать extends и include
Рассмотрим общие правила на примере include для файла _card.html  c вызовом из index.html.

- `_card.html`:  имя файла имеет префикс «_» что объявляет его вспомогательным, а значит при его изменении будут рендерится и все файлы в которых есть к нему обращение, а сам он не будет переносится в /build

- Передача значений  переменных на примере page и  number.

```html
{% with page="Домашняя", number=1 %}
  {% include "_card.html" %}
{% endwith %}
```

- Пример строки в файле _card.html с переменными page и  number.
  
```html
<p>Вывод текста из файла _card.html методом include. Страница {{page}} Номер {{number}} </p>
```

<img width="738" alt="image" src="https://github.com/SGKespace/StaticJinjaPlus/assets/55636018/6fbce118-e5ae-46b8-b5e5-7ab4df323562">


## Example templates
The repository has example templates to see how StaticJinjaPlus works.

Run the following command and see your results in `./build`:
```commandline
python main.py --srcpath example/templates
```
```shell
build
├── about.html
├── assets
│  └── style.css
├── faq.html
└── index.html

```
![Example of index.html](https://imgur.com/Onr3aVM.jpg)
Example render of `index.html`

