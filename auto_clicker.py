#!/usr/bin/env python3

import os
os.system('clear')

import pyautogui
import time
# import keyboard

stop = False

'''
def exit_check(event):
    global stop
    if event.name == 'q':
        print('Stopping Clicker')
        stop = True
'''

# keyboard.on_press(exit_check)
x=0
while True:
#while x<100:
#    if stop == True:
#        break
    print(pyautogui.position()) 
    pyautogui.click()
    #time.sleep(.01)
#    x+=1











exit()
