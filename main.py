import argparse
from pathlib import Path

from staticjinja import Site

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-w",
        "--watch",
        help="Render the site, and re-render on changes to <srcpath>",
        action="store_true"
    )
    parser.add_argument(
        "--srcpath",
        help="the directory to look in for templates (defaults to './templates)'",
        default=Path(".").joinpath("templates")
    )
    parser.add_argument(
        "--outpath",
        help="the directory to place rendered files in (defaults to '.')",
        default=Path(".")
    )
    parser.add_argument(
        "--static",
        help="the directory (or directories) within srcpath where static files (such as CSS and JavaScript) "
             "are stored. Static files are copied to the output directory without any template compilation, "
             "maintaining any directory structure. This defaults to None, meaning no files are considered to "
             "be static files. You can pass multiple directories separating them by commas:"
             " --static=\"foo,bar/baz,lorem\""
    )
    args = parser.parse_args()

    site = Site.make_site(
        searchpath=args.srcpath,
        outpath=args.outpath,
    )
    
    site.render(use_reloader=args.watch)
