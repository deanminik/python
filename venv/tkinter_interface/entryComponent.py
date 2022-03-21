import tkinter as tk
# import the module of the tkinder theme
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Entry components')


window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=10)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=5)

# define a variable to modify after(set), (get)
entry_var1 = tk.StringVar(value='Value by default')
entry1 = ttk.Entry(window, width=30 , textvariable=entry_var1)
entry1.grid(row=0,column=0)
# insert
#entry1.insert(0,'Add a text')
#entry1.insert(tk.END, '.') # add at the end this tex
#entry1.config(state='readonly')


# Create a btn to get the data from the entry
def send():
    # recover the data from variable
    btn1.config(text=entry_var1.get())
    # modify with set
    entry_var1.set('Changing...')
    # recover
    print(entry_var1.get())
    print(entry1.get())



btn1 = ttk.Button(window, text='SEND', command=send)
btn1.grid(row=0,column=1)
window.mainloop()
