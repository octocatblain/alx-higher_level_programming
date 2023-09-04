#!/usr/bin/python3
"""Say my name module"""


def say_my_name(first_name, last_name=""):
    """Prints a name"""

    #  ERROR MESSAGE DICT  #
    err_msg = {
        "FirstNotStr": "first_name must be a string",
        "LastNotStr": "last_name must be a string",
    }
    #  TESTS  #
    if type(first_name) != str:
        raise TypeError(err_msg["FirstNotStr"])
    if type(last_name) != str:
        raise TypeError(err_msg["LastNotStr"])

    #  OUTPUT  #
    print(f"My name is {first_name}", end="")
    if len(last_name) == 0:
        print()
    else:
        print(f" {last_name}")
