import argparse


def cli():
    parser = argparse.ArgumentParser(
        description="Gather all your osu! songs, renamed properly, into a single directory",
        allow_abbrev=False,
        add_help=True,
    )
    parser.version = '0.1.0'

    parser.add_argument(
        "osu",
        type=str,
        help="your osu! directory"
    )
    parser.add_argument(
        "dest",
        type=str,
        help="the folder the songs will be copied to"
    )

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        help="queries the version"
    )
    return parser
