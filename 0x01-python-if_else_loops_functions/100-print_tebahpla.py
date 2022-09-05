#!/usr/bin/python3
for i in range(0, 26):
    if i % 2 == 0:
        unicode_point = 122 - i
    else:
        unicode_point = 90 - i
    c = chr(unicode_point)
    print("{}".format(c), end='')
