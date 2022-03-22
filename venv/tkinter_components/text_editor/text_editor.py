import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfilename

class Editor(tk.Tk):
    def __init__(self):
        super(Editor, self).__init__()
        #super().__init__() # we can use both
        self.title('Text Editor')
        # min size of the window
        self.rowconfigure(0,minsize=600, weight=1)
        # config min size of the second column
        self.columnconfigure(1, minsize=600, weight=1)
        # Attribute text area
        self.text_area = tk.Text(self, wrap=tk.WORD)
        # Attribute file
        self.file = None
        # Attribute to know if this opened before
        self.file_opened = False
        # creation of components so we call this object or method
        self._create_components()
        # create menu
        self._menu()



    def _create_components(self):
        frame_btn = tk.Frame(self, relief=tk.RAISED, bd=2)
        btn_open = tk.Button(frame_btn, text='Open', command=self._open_file)
        btn_save = tk.Button(frame_btn, text='Save', command=self._save)
        btn_save_as = tk.Button(frame_btn, text='Save as',command=self._save_as)
        # all btn expand horizontal (sticky=WE)
        btn_open.grid(row=0, column=0, sticky='WE', padx=5 , ipady=5)
        btn_save.grid(row=1, column=0, sticky='WE', padx=5 , ipady=5)
        btn_save_as.grid(row=2, column=0, sticky='WE', padx=5 , ipady=5)
        # we place the frame vertically North to South
        frame_btn.grid(row=0, column=0, sticky='NS')
        # expand the text area completely
        self.text_area.grid(row=0, column=1 ,sticky='NSEW') # Cover from north, south, east  and west

    def _menu(self):
        # create the menu of the app
        menu_app = tk.Menu(self)
        self.config(menu=menu_app)
        # add the options to our menu
        #-> add file menu
        file_menu = tk.Menu(menu_app, tearoff=False) # tearoff -> do not let to separate from the container
        menu_app.add_cascade(label='File', menu=file_menu)
        # -> add more options of the file menu
        file_menu.add_command(label='Open', command=self._open_file)
        file_menu.add_command(label='Save', command=self._save)
        file_menu.add_command(label='Save as...', command=self._save_as)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)

    def _open_file(self):
        # pass
        # open the file for edition
         self.file_opened = askopenfile(mode='r+') # r -> read + -> edit
        # delete the text
         self.text_area.delete(1.0, tk.END) # 1.0 -> from the line one to the end of the text
        # check if there a file
         if not self.file_opened:
             return
        # open the file to read
         with open(self.file_opened.name, 'r+') as self.file: # name to take the file you want
             # read the content
             text = self.file.read()
             # insert the info from the file in the text area
             self.text_area.insert(1.0, text)
             # modify the title of the app
             self.title(f'*Text editor - {self.file.name}')


    def _save(self):
        #pass
        # if we already opened a file, we will overwrite
        # ask if we have data
        if self.file_opened:
            # save the file
            with open(self.file_opened.name, 'w') as self.file:
                # read the content from the text area
                text = self.text_area.get(1.0, tk.END)
                # We write the content to the same file
                self.file.write(text)
                # change the title name of the app
                self.title(f'Text editor - {self.file.name}')
        else:
            self._save_as()



    def _save_as(self):
        # pass
        # save as new file
        self.file = asksaveasfilename(
            defaultextension='.txt',
            filetypes=[('Text files', '*.txt'), ('All files', '*.*')]
            # *.txt -> show all text files (*-> no matter the name .*-> no mather the extension  )
        )
        if not self.file:
            return

        #open the file in write mode
        with open(self.file, 'w') as self.file:
            # read the content of the text area
            text = self.text_area.get(1.0, tk.END)
            # write the content to the new file
            self.file.write(text)
            # change the name of te file
            self.title(f'Text editor - {self.file}')
            # we indicate we have opened a file
            self.file_opened = self.file


if __name__ == '__main__':
    editor = Editor()
    editor.mainloop()