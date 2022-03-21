# Components
import tkinter as tk
from tkinter import ttk, messagebox

window = tk.Tk()
window.geometry('600x400')
window.title('Components')


def create_tabs():
    # create a control tab unsing a class notebook
    control_tab = ttk.Notebook(window)
    # frame -> to add more components
    tab1 = ttk.Frame(control_tab)
    # add the tab to control tab
    control_tab.add(tab1, text='Tabulation 1')
    # Show this tab
    control_tab.pack(fill='both') # fill='both'-> fill with the all space up and down section

    #Add a label and a component of entry
    label1 = ttk.Label(tab1, text='Name:')
    label1.grid(row=0, column=0, sticky=tk.E)
    entry1 = ttk.Entry(tab1, width=30)
    entry1.grid(row=0, column=1, padx=5, pady=5)
    # add btn
    def send():
        messagebox.showinfo('Message', f'Name: {entry1.get()}')
    btn1 = ttk.Button(tab1, text='Send', command=send)
    btn1.grid(row=1, column=0, columnspan=2)

create_tabs()
window.mainloop()



