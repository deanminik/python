import tkinter as tk
from tkinter import messagebox

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('450x450')
        self.resizable(0,0) # to do not resize the window
        self.title('Calculator')

        # define attributes
        self.expression = ''
        # Box text
        self.entry = None
        # String var to get or update the input value
        self.entry_text = tk.StringVar()
        # Create components
        self._creation_components()

    # Class Method
    def _creation_components(self):
        # create frame 1
        entry_frame = tk.Frame(self, width=450, height=50, bg='grey') # This is like a div
        # ->  Publish the frame
        entry_frame.pack(side=tk.TOP)
        # ->  Adding the box text component
        entry = tk.Entry(entry_frame, font=('arial', 18, 'bold'),
                         textvariable=self.entry_text, width=33, justify=tk.RIGHT)
        # -> Publish this entry component
        entry.grid(row=0, column=0, ipady=10)
        #**********************************************************************************************

        # create Frame 2
        frame_2_for_btns = tk.Frame(self, width=400, height=450, bg='grey')
        frame_2_for_btns.pack()


        # Row -> 1 FROM THE FRAME 2
        btn_clean = tk.Button(frame_2_for_btns, text='C', width=37, height=3,
                              bd=0, bg='#eee', cursor='hand2', command=self._clean_event)
            # -cursor='hand1' https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/cursors.html
        #   publish
        btn_clean.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

        btn_division = tk.Button(frame_2_for_btns, text='/', width=10, height=3,
                              bd=0, bg='#eee', cursor='hand2', command=lambda: self._click_event('/')
                                 ).grid(row=0, column=3, padx=1, pady=1)
            # lambda: -> anonymous function
                # we use the lambda because in this case we need to add a parameter. And to do not call
                # the function and keep just the reference
                # so, now we can add parameters

        # Row -> 2 from the FRAME 2
        btn_7 = tk.Button(frame_2_for_btns, text='7', width=10, height=3,
                              bd=0, bg='#fff', cursor='hand2', command=lambda: self._click_event('7')
                                 ).grid(row=1, column=0, padx=1, pady=1)
        btn_8 = tk.Button(frame_2_for_btns, text='8', width=10, height=3,
                          bd=0, bg='#fff', cursor='hand2', command=lambda: self._click_event('8')
                          ).grid(row=1, column=1, padx=1, pady=1)
        btn_9 = tk.Button(frame_2_for_btns, text='9', width=10, height=3,
                          bd=0, bg='#fff', cursor='hand2', command=lambda: self._click_event('9')
                          ).grid(row=1, column=2, padx=1, pady=1)
        btn_Mul = tk.Button(frame_2_for_btns, text='*', width=10, height=3,
                          bd=0, bg='#eee', cursor='hand2', command=lambda: self._click_event('*')
                          ).grid(row=1, column=3, padx=1, pady=1)
        # Row -> 3 from the FRAME 2
        btn_4 = tk.Button(frame_2_for_btns, text='4', width=10, height=3,
                          bd=0, bg='#fff', cursor='hand2', command=lambda: self._click_event('4')
                          ).grid(row=2, column=0, padx=1, pady=1)
        btn_5 = tk.Button(frame_2_for_btns, text='5', width=10, height=3,
                          bd=0, bg='#fff', cursor='hand2', command=lambda: self._click_event('5')
                          ).grid(row=2, column=1, padx=1, pady=1)
        btn_6 = tk.Button(frame_2_for_btns, text='6', width=10, height=3,
                          bd=0, bg='#fff', cursor='hand2', command=lambda: self._click_event('6')
                          ).grid(row=2, column=2, padx=1, pady=1)
        btn_Subtraction = tk.Button(frame_2_for_btns, text='-', width=10, height=3,
                            bd=0, bg='#eee', cursor='hand2', command=lambda: self._click_event('-')
                            ).grid(row=2, column=3, padx=1, pady=1)

        # Row -> 4 from the FRAME 2

        btn_1 = tk.Button(frame_2_for_btns, text='1', width=10, height=3,
                          bd=0, bg='#fff', cursor='hand2', command=lambda: self._click_event('1')
                          ).grid(row=3, column=0, padx=1, pady=1)
        btn_2 = tk.Button(frame_2_for_btns, text='2', width=10, height=3,
                          bd=0, bg='#fff', cursor='hand2', command=lambda: self._click_event('2')
                          ).grid(row=3, column=1, padx=1, pady=1)
        btn_3 = tk.Button(frame_2_for_btns, text='3', width=10, height=3,
                          bd=0, bg='#fff', cursor='hand2', command=lambda: self._click_event('3')
                          ).grid(row=3, column=2, padx=1, pady=1)
        btn_Sum = tk.Button(frame_2_for_btns, text='+', width=10, height=3,
                                    bd=0, bg='#eee', cursor='hand2', command=lambda: self._click_event('+')
                                    ).grid(row=3, column=3, padx=1, pady=1)
        # Row -> 5 from the FRAME 2
        btn_0 = tk.Button(frame_2_for_btns, text='0', width=24, height=3,
                          bd=0, bg='#fff', cursor='hand2', command=lambda: self._click_event('0')
                          ).grid(row=4, column=0, columnspan=2)
        btn_dot = tk.Button(frame_2_for_btns, text='.', width=10, height=3,
                          bd=0, bg='#eee', cursor='hand2', command=lambda: self._click_event('.')
                          ).grid(row=4, column=2, padx=1, pady=1)
        btn_equal = tk.Button(frame_2_for_btns, text='=', width=10, height=3,
                           bd=0, bg='#eee', cursor='hand2', command=self._check_event
                           ).grid(row=4, column=3, padx=1, pady=1)                                

    def _clean_event(self):
        self.expression = ''
        self.entry_text.set(self.expression)

    def _click_event(self,element):
        # concatenate the new element to expression
        self.expression = f'{self.expression}{element}'
        #update the input
        self.entry_text.set(self.expression)
        
    def _check_event(self):
        try:
            if self.expression:
                # eval -> Execution of a string number or operation. Example: "3+4" -> expression
                result = str(eval(self.expression))
                # update
                self.entry_text.set(result)
        except Exception as e:
            messagebox.showerror('Error', f'There was an error: {e}')
            self.entry_text.set('')
        finally:  # or is there another error put back an empty space too 
            self.expression = ''


        

if __name__ == '__main__':
    cal = Calculator()
    cal.mainloop()

