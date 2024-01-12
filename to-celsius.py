#!/usr/bin/env python3

import os
os.system('clear')


fahren = float(input("What is the temperature in Fahrenheit? "))
celsius = float(round(float((fahren-32)*5/9), 4))

print(fahren, "in Fahrentheit is", celsius, "in Celsius.")



exit()
