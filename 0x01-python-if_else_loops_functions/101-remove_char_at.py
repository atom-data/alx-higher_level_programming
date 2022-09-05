#!/usr/bin/python3
def remove_char_at(str, n):
    "Remove characters at position n"
    if n >= 0:
        newstring = str[:n] + str[n + 1:]
        return newstring
    else:
        return str
