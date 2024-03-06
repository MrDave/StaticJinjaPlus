import argparse
from pathlib import Path

from staticjinja import Site


def main():
    parser = argparse.ArgumentParser(
        description="Render HTML pages from Jinja2 templates"
    )
    parser.add_argument(
        "-w",
        "--watch",
        help="Render the site, and re-render on changes to <srcpath>",
        action="store_true"
    )
    parser.add_argument(
        "--srcpath",
        help="The directory to look in for templates (defaults to './templates)'",
        default=Path(".") / "templates",
        type=Path
    )
    parser.add_argument(
        "--outpath",
        help="The directory to place rendered files in (defaults to './build')",
        default=Path(".") / "build",
        type=Path
    )

    args = parser.parse_args()

    src_path = args.srcpath
    output_path = args.outpath
    static_path = Path(src_path) / "assets"

    site = Site.make_site(
        searchpath=src_path,
        outpath=output_path,
        staticpaths=[static_path]
    )

    site.render(use_reloader=args.watch)


if __name__ == '__main__':
    main()
