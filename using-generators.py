#!/usr/bin/env python3

import os
os.system('clear')

def char_range(start, stop, step=1):
    start_code  = ord(start)
    stop_code = ord(stop)
    stop_modifier = 1

    if start_code > stop_code:
        step *= -1
        stop_modifier *= -1


    for value in range(start_code, stop_code + stop_modifier, step):
        yield chr(value)




exit()
