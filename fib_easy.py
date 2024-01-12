#!/usr/bin/env python3

import os
os.system('clear')

counter = int(input('What number in the Fibonacci sequence would you like to calculate?  '))

num1 = 0
num2 = 1

for i in range(counter-1):
    num1, num2 = num2, num1 + num2

print(num2)


exit()
