#!/usr/bin/env python3

import os
os.system('clear')

numb = int(input('How high do you want to test FizzBuzz using whole numbers?  '))

if numb < 1:
    print('You need to use a number 1 or higher')
    exit()


for i in range(1, numb + 1):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)




exit()
