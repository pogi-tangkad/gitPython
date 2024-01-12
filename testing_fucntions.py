#!/usr/bin/env python3

import os
os.system('clear')


def split_name(name):
    first_name, last_name = name.split(maxsplit=1)
    return {
        'first_name': first_name,
        'last_name': last_name,
    }

assert split_name('Kevin Bacon') == {
    'first_name': 'Kevin',
    'last_name': 'Bacon',
}, f"Expected {{'first_name': 'Kevin', 'last_name': 'Bacon'}} but received {split_name('Kevin Bacon')}"

print(split_name('Kevin Repking'))


assert split_name('Victor Von Doom') == {
    'first_name': 'Victor',
    'last_name': 'Von Doom',
}, f"Expected {{'first_name': 'Victor', 'last_name': 'Von Doom'}} but received {split_name('Victor Von Dooom')}"

print(split_name('Victor Von Doom'))


def is_palindrome(palin):
    return str(palin) == str(palin)[::-1]

assert is_palindrome('radar') == True, f"Expected True but got {is_palindrome('radar')}"
print(is_palindrome('radar'))

assert is_palindrome('stop') == False, f"Expected False but got {is_palindrome('stopots')}" 
print(is_palindrome('stop'))

assert is_palindrome(101) == True, f"Expected True but got {is_palindrome(101)}"
print(is_palindrome(101))

assert is_palindrome(10) == False, f"Expected False but got {is_palindrome(10)}"
print(is_palindrome(10))




def build_list(item, count=1):
    items = []
    for _ in range(count):
        items.append(item)
    return items

print(build_list('booger', 20))
print(build_list('nacho'))


assert build_list("Apple", 3) == [
    "Apple",
    "Apple",
    "Apple",
], f"Expected ['Apple', 'Apple', 'Apple'] but received {repr(build_list('Apple', 3))}"
assert build_list("Orange") == [
    "Orange"
], f"Expected ['Orange'] but received {repr(build_list('Orange'))}"



exit()
