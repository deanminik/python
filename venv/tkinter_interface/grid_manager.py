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
def event4():
    btn4.config(text='Pressed button', fg='blue', relief=tk.GROOVE, bg='yellow')
    # we can't use this  fg='blue', relief=tk.GROOVE with ttk from the theme




#define 2 btn
btn1 = ttk.Button(window, text='Button 1', command=event1)
#btn1.pack()
#btn1.grid(row=0, column=0)
btn1.grid(row=0, column=0, sticky='NSWE', padx=40, pady=30, ipady=50, columnspan=2, rowspan=2) # NSWE -> get the all space available
"""
padx -> extern padding 
pady
ipadx -> inter padding
ipady
"""

"""
to work with sticky 
N -> up
E -> right
S -> down
W -> left
"""

#btn2 = ttk.Button(window, text='Button 2', command=event2)
#btn2.grid(row=1, column=0, sticky='NSWE')

#btn3 = ttk.Button(window, text='Button 3')
#btn3.grid(row=0, column=1, sticky='NSWE')

#USING TK directly
#btn4 = tk.Button(window, text='Button 4', command=event4)
#btn4.grid(row=1, column=1, sticky='NSWE')
window.mainloop()
