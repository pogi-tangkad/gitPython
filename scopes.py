#!/usr/bin/env python3

import os
os.system('clear')

# if 1 < 2:
#     x = 5


y = 5


def set_x(z):
    x = z
    global y
    global a
    y = x
    a = 7


print("y before set_x:", y)

set_x(10)

print("y after set_x:", y)
print("a after set_x:", a)

# print("Outer y:", y)




# while x < 6:
#     print(x)
#     x += 1

# print(x)











exit()
