import tkinter as tk
# import the module of the tkinder theme
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Grid Manager')

# define events methods
def event1():
    btn1.config(text='Pressed button')
def event2():
    btn2.config(text='Pressed button')

#define 2 btn
btn1 = ttk.Button(window, text='Button 1', command=event1)
#btn1.pack()
btn1.grid(row=0, column=0)


btn2 = ttk.Button(window, text='Button 2', command=event2)
btn2.grid(row=1, column=0)
window.mainloop()
