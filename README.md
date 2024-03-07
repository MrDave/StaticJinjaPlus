# StaticJinjaPlus

StaticJinjaPlus is a tool to build static sites using Jinja2

## How to install

Python should already be installed. This project is tested on Python 3.11. You may use other versions as you will, but YMMV.

Clone the repo / download code

Using virtual environment [virtualenv/venv](https://docs.python.org/3/library/venv.html) is recommended for project isolation.

Install requirements:
```commandline
$ pip install -r requirements.txt
```

## Building sites

To render html pages from templates, run
```commandline
$ python main.py
```
This will look in `./templates` for templates (files whose name does not start with `.` or `_`) and build them to `./build`

You'll see a message about each template in the output:
```commandline
Rendering index.html...
```

To watch for changes in the templates and recompile build files if changes happen, use `-w` or `--watch` argument
```commandline
$ python main.py -w

Rendering index.html...
Watching '/home/mrdave/Python Projects/StaticJinjaPlus/templates' for changes...
Press Ctrl+C to stop.
```

### Specifying templates or build paths

To change the source and/or output paths use optional arguments  
- `--srcpath` - the directory to look in for templates (defaults to `./templates`)  
- `--outpath` - the directory to place rendered files in (defaults to `.`)

Example:
```commandline
$ python main.py --srcpath other_template_folder --outpath ./built/site

Rendering index.html...
```

### Using assets

To use assets such as `.css` and `.js` files with your templates, place them in `assets` folder inside source path (so `./templates/assets` by default)
In this case StaticJinjaPlus will copy the assets to output folder keeping the same relative paths

Building log will also include "rendering" the assets:

```commandline
$ python main.py
Rendering assets/style.css...
Rendering index.html...
```