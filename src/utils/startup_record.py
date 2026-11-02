from os import path
from sys import argv


def get_startup_record_path(args=None):
    """Return the macro file passed on the command line, or None when there is none.

    Arguments that are not an existing file (e.g. `--help` or `/?`) are ignored.
    """
    args = argv if args is None else args
    if len(args) > 1 and path.isfile(args[1]):
        return args[1]
    return None
