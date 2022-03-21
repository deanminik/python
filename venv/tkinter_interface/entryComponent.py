import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('handle components')


window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=10)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=5)

# define a variable to modify after(set), (get)
entry_var1 = tk.StringVar(value='Value by default')
entry1 = ttk.Entry(window, width=30 , textvariable=entry_var1)
entry1.grid(row=0,column=0)
#labels
label1 = tk.Label(window, text='Here will show the content of the box')
label1.grid(row=1, column=0, columnspan=2) # columnspan=2 -> use two column


# Create a btn to get the data from the entry
def send():
    label1.config(text=entry_var1.get())


btn1 = ttk.Button(window, text='SEND', command=send)
btn1.grid(row=0,column=1)
window.mainloop()
