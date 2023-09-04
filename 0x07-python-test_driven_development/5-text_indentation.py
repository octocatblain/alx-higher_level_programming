#!/usr/bin/python3
"""Text indentation module"""


def text_indentation(text):
    """function that prints a text with new lines"""

    last = " "
    string = ""
    if text == "":
        print(string, end="")
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i is last and i == " ":
            last = i
            continue
        if last in [".", "?", ":"] and i == " ":
            last = i
            continue
        string += i + "\n" + "\n" if i in [".", "?", ":"] else i
        last = i
    print(string.rstrip(" "), end="")
