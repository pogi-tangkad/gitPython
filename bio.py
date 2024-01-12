#!/usr/bin/env python3


name = input("What is your name? ")
color = input("What is your favorite color? ")
age = int(input("What is your age? "))

# print(name, end=" ")
# print("is " + str(age) + " years old", end=" ")
# print("and loves the color " + color + ".")

print(name, 'is', age, 'years old and loves the color', color + '.', sep=" ")






exit()
