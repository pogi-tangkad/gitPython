#!/usr/bin/env python3

# clear the screen using the linux command 'clear'

import os
os.system('clear')


# Prompt the user for a number and store it as a variable

fizz_num = int(input('Enter a whole number: '))

# print(fizz_num)          #quick check to make sure the input variable sets correctly


# test the user input to see if it is divisible by 3 or 5 or both.
# print a response based on the results of the test

if (fizz_num % 3) == 0 and (fizz_num % 5) == 0:
    print('FizzBuzz')
elif (fizz_num % 3) == 0:
    print('Fizz')
elif (fizz_num % 5) == 0:
    print('Buzz')
else:
    print('No Soda Honey for you')


# Prompt user if they would like to see all possible results
# from 1 to 100

looper1 = 1                 # set the counter variable

if input('Would you like to see all possibilities from 1 - 100? (yes or no)  ').lower()[0] == 'y':
    while looper1 <=100:
#        do:
        if (looper1 % 3) == 0 and (looper1 % 5) == 0:
            print(looper1, '= FizzBuzz')
        elif (looper1 % 3) == 0:
            print(looper1, '= Fizz')
        elif (looper1 % 5) == 0:
            print(looper1, '= Buzz')
        else:
            print(looper1, '= No Soda Honey for you')

        looper1 += 1        # incriment the counter by 1
#        done:
else:
    print('OK.  Goodbye')

           


exit()
