# Components
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from time import sleep
window = tk.Tk()
window.geometry('600x400')
#window.geometry('600x400+200+500') # x and y position
window.title('Components')


def create_components_tab_1(tab):
    # Add a label and a component of entry
    label1 = ttk.Label(tab, text='Name:')
    label1.grid(row=0, column=0, sticky=tk.E)
    entry1 = ttk.Entry(tab, width=30)
    entry1.grid(row=0, column=1, padx=5, pady=5)

    # add btn
    def send():
        messagebox.showinfo('Message', f'Name: {entry1.get()}')

    btn1 = ttk.Button(tab, text='Send', command=send)
    btn1.grid(row=1, column=0, columnspan=2)

def create_components_tab_2(tab):
    content = 'This my text we the content'
    #create the scroll component
    scroll = scrolledtext.ScrolledText(tab, width=50, height=10, wrap=tk.WORD) # wrap=tk.WORD -> to show completed words
    scroll.insert(tk.INSERT, content)
    #show the scroll component
    scroll.grid(row=0, column=0)

def create_components_tab_3(tab):
    # create a list with data list comprehension
    data = [x+1 for x in range(10)] # x+1 -> to start from 1 end finish in 10
    combobox = ttk.Combobox(tab, width=15, values=data)
    combobox.grid(row=0, column=0, padx=10, pady=10)
    # select an element by default to show
    combobox.current(5) # this will present the 6 or just add (- 1) to have 5 - 1 to get 5
    # add a btn to know the option of the user
    def showValue():
        messagebox.showinfo('Selected value', f'Selected value: {combobox.get()}')

    btn1 = ttk.Button(tab, text='Show selected value', command=showValue)
    btn1.grid(row=0, column=1)

def create_components_tab_4(tab):
    # imagen component
    def show_title():
        messagebox.showinfo('MOre info of the image', f'Image name: {imagen.cget("file")}')
    imagen  = tk.PhotoImage(file='python-logo.png')
    btn_image = ttk.Button(tab, image=imagen, command=show_title)
    btn_image.grid(row=0, column=0)

def create_components_tab_5(tab):
    # create the component progress bar
    progress_bar = ttk.Progressbar(tab, orient='horizontal', length=550)
    progress_bar.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

    def executeBar():
        progress_bar['maximum'] = 100 # complete the bar
        for value in range(101):
            # wait a bit before to execute the bar
            sleep(0.05)
            # increment our progress bar
            progress_bar['value'] = value
            # update the progress bar
            progress_bar.update()
        progress_bar['value'] = 0

    def executeLoop():
        progress_bar.start()
    def stop():
        progress_bar.stop()
    def stopAfter():
        wait_ms = 1000
        window.after(wait_ms, progress_bar.stop())
    # handle the events of a progress bar
    btn_start = ttk.Button(tab, text='Execute progress bar', command=executeBar)
    btn_start.grid(row=1, column=0)
    btn_loop = ttk.Button(tab, text='Execute loop', command=executeLoop)
    btn_loop.grid(row=1, column=1)
    btn_stop = ttk.Button(tab, text='Stop execution', command=stop)
    btn_stop.grid(row=1, column=2)
    btn_after = ttk.Button(tab, text='Stop execution after this time', command=stopAfter)
    btn_after.grid(row=1, column=3)

def create_tabs():
    # create a control tab unsing a class notebook
    control_tab = ttk.Notebook(window)
    # frame -> to add more components
    tab1 = ttk.Frame(control_tab)
    # add the tab to control tab
    control_tab.add(tab1, text='Tabulation 1')
    # Show this tab
    control_tab.pack(fill='both') # fill='both'-> fill with the all space up and down section
    # create components of tab1
    create_components_tab_1(tab1)
    # second tab
    tab2 = ttk.Labelframe(control_tab, text='Content')
    control_tab.add(tab2, text='Tabulation 2')
    # create the components of the second tab
    create_components_tab_2(tab2)
    # Create the third tab
    tab3 = ttk.Frame(control_tab)
    control_tab.add(tab3, text='Tabulation 3')
    # create the components of the third tab
    create_components_tab_3(tab3)
    # fourth tab
    tab4 = ttk.LabelFrame(control_tab, text='Image')
    control_tab.add(tab4, text='Tabulation 4')
    # Create the components of the fourth tab
    create_components_tab_4(tab4)
    # fifth tab
    tab5 = ttk.LabelFrame(control_tab, text='Progress bar')
    control_tab.add(tab5, text='Tabulation 5')
    # create components of the fifth tab
    create_components_tab_5(tab5)




create_tabs()
window.mainloop()



