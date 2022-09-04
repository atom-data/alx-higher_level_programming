#!/usr/bin/python3
def islower(c):
    """Check for lowercase characters"""
    unicode_point = ord(c)
    if unicode_point >= 97 and unicode_point <= 122:
        return True
    else:
        return False
