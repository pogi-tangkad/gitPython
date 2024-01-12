import tkinter as tk
from time import sleep

ender = True

def quitter():
    global ender
    ender = False
    return ender

dir_x = 8
dir_y = 11
pos_x = 20
pos_y = 20

root = tk.Tk()
root.geometry('500x500')

button1 = tk.Button(root, text='Test1', pady=10, padx=50, command=quitter)
button2 = tk.Button(root, text='Test2', pady=10, padx=50, command=quitter)
button3 = tk.Button(root, text='Test3', pady=10, padx=50, command=quitter)
button4 = tk.Button(root, text='Test4', pady=10, padx=50, command=quitter)

while ender:

    button1.place(x=root.winfo_width()-button1.winfo_width()-10,
                  y=10, anchor='ne')
    button2.place(x=root.winfo_width()-10,
                  y=10, anchor='ne')
    button3.place(x=root.winfo_width()-button1.winfo_width()-10,
                  y=button1.winfo_height()+10, anchor='ne')
    button4.place(x=root.winfo_width()-10,
                  y=button1.winfo_height()+10, anchor='ne')
    root.minsize(button1.winfo_width()*3, button1.winfo_height()*3)
    root.update()
    sleep(.1)

root.destroy()
root.mainloop()