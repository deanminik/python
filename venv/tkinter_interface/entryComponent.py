import tkinter as tk
# import the module of the tkinder theme
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Entry components')

# grid configuration adding lines sizes
# first row
window.rowconfigure(0, weight=1)
# second row
window.rowconfigure(1, weight=10)
# first column
window.columnconfigure(0, weight=1)
# second column
window.columnconfigure(1, weight=5)

# width is the count of characters that the box needs to expand
entry1 = ttk.Entry(window, width=30 , justify=tk.CENTER)
entry1.grid(row=0,column=0)
# insert
entry1.insert(0,'Add a text')
entry1.insert(tk.END, '.') # add at the end this tex
#entry1.config(state='readonly')


# Create a btn to get the data from the entry
def send():
    print(entry1.get())
    btn1.config(text=entry1.get()) # changing the text button
    ### delete te content
    #entry1.delete(0, tk.END)
    # select the text of ou box
    entry1.select_range(0, tk.END) # -> From zero to the end
    #to make it possible call the focus method
    entry1.focus()

btn1 = ttk.Button(window, text='SEND', command=send)
btn1.grid(row=0,column=1)
window.mainloop()

"""
Entry elements:
width=30 , 
justify=tk.CENTER, 
show='*'
state=tk.DISABLED
"""