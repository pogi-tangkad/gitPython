#!/usr/bin/env python3


import os
os.system('clear')





my_str = input('Input a string: ')

print('All lower case: ', my_str.lower())
print('All upper case: ', my_str.upper())
print('Title case:     ', my_str.title())
print('Capitalized:    ', my_str.capitalize())

my_list = my_str.split()
print('Each word', my_list)

alpha_list = sorted(my_list)
print('Each word in alphabetical order: ', alpha_list)


print('The first word in alphabetical order is: ', alpha_list[0])
print('The last word in alphabetical order is: ', alpha_list[-1])



exit()
