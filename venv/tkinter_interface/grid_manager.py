import tkinter as tk
# import the module of the tkinder theme
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Grid Manager')

# grid configuration adding lines sizes
# first row
window.rowconfigure(0, weight=1)
# second row
window.rowconfigure(1, weight=10)
# first column
window.columnconfigure(0, weight=1)
# second column
window.columnconfigure(1, weight=5)


# define events methods
def event1():
    btn1.config(text='Pressed button')
def event2():
    btn2.config(text='Pressed button')

#define 2 btn
btn1 = ttk.Button(window, text='Button 1', command=event1)
#btn1.pack()
#btn1.grid(row=0, column=0)
btn1.grid(row=0, column=0, sticky='NSWE') # NSWE -> get the all space available

"""
to work with sticky 
N -> up
E -> right
S -> down
W -> left
"""

btn2 = ttk.Button(window, text='Button 2', command=event2)
btn2.grid(row=1, column=0, sticky='NSWE')

btn3 = ttk.Button(window, text='Button 3')
btn3.grid(row=0, column=1, sticky='NSWE')

btn4 = ttk.Button(window, text='Button 4')
btn4.grid(row=1, column=1, sticky='NSWE')
window.mainloop()
