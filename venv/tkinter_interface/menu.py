import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

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
label1.grid(row=1, column=0, columnspan=2)

def send():
    label1.config(text=entry1.get())
    mens1 = entry1.get()
    messagebox.showinfo('windows title Message data', mens1 + 'Informatics')

def exitEvent():
    window.quit()
    window.destroy() # important to delete the object
    print('We are out of this application')
    sys.exit()

def create_menu():
    # main menu
    main_menu = Menu(window)
    # tearoff = False -> this is to do not separate the menu in our interface
    sub_file_menu = Menu(main_menu, tearoff=False)
    # Add a new option to the menu
    sub_file_menu.add_command(label='New')
    #separator
    sub_file_menu.add_separator()
    # exit option
    sub_file_menu.add_command(label='Exit', command=exitEvent)
    # Add the submenu to the main menu
    main_menu.add_cascade(menu=sub_file_menu, label='File')
    # help submenu
    sub_menu_help = Menu(main_menu, tearoff=False)
    # adding a new option
    sub_menu_help.add_command(label='About')
    # add to the main menu this submenu
    main_menu.add_cascade(menu=sub_menu_help, label='Help')
    #Show the menu in the main window
    window.config(menu=main_menu)




btn1 = ttk.Button(window, text='SEND', command=send)
btn1.grid(row=0,column=1)

create_menu()
window.mainloop()

