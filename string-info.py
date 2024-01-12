#!/usr/bin/env python3

message = input("Enter a message: ")

print("The First character is: ", message[0])
print("The Middles character is: ", message[int(len(message)/2)])
print("The Last character is: ", message[-1])
print("Even index characters: ", message[1::2])
print("Odd index characters: ", message[::2])
print("Reversed message: ", message[::-1])




exit()
