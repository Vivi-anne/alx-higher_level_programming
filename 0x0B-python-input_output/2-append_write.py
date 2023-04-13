#!/usr/bin/python3
"""modules defines a file-appending function."""


def append_write(filename="", text=""):
    """ appends to the end of the text file.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
