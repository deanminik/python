# GUI -> Graphical User Interface
# there are another package to create interface, not just Tkinder

# if you get an error apply thi command
## sudo apt-get install python3-tk
import tkinter as tk
# import the module of the tkinder theme
from tkinter import ttk

# we create an object using TK
window = tk.Tk()
# modify the size of the window (px)
window.geometry('600x400')
# name of the window
window.title('New window')
#configure the icon -> .xbm for linux also adding @, end ico for windows
window.iconbitmap('@icono.xbm')
# the (window.iconbitmap('@icono.xbm') does not show the icon -> issue

# a btn -> widget or component, the window is the father object
# before to create this btn we define the event click
def event_click():
    print('Execution of the click event')
    btn1.config(text='changed')
    # creating a new component
    btn2 = ttk.Button(window, text='new button')
    btn2.pack()

btn1 = ttk.Button(window, text='click', command=event_click)
# -> use pack layout manager to show thw btn
btn1.pack()



# execute at the end to see the changes
window.mainloop()
