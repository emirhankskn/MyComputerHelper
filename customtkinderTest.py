import customtkinter

### GRID SYSTEM
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Grid System')
        self.geometry('600x150')
        self.grid_columnconfigure((0, 2), weight=1)
        
        self.button = customtkinter.CTkButton(self, text='My Button', command=self.button_callback)
        self.button.grid(row=0, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

        self.chkBox1 = customtkinter.CTkCheckBox(self, text='CheckBox 1')
        self.chkBox1.grid(row=1, column=0, padx=10, pady=(0,10), sticky='w')

        self.chkBox2 = customtkinter.CTkCheckBox(self, text='CheckBox 2')
        self.chkBox2.grid(row=1, column=1, padx=10, pady=(0,10))

        self.chkBox3 = customtkinter.CTkCheckBox(self, text='CheckBox 3')
        self.chkBox3.grid(row=1, column=2, padx=10, pady=(0,10), sticky='e')

    def button_callback():
        print('Button pressed...')

app = App()
app.mainloop()



### USING FRAMES
class MyCheckBoxFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.chk1 = customtkinter.CTkCheckBox(self, text='Checkbox 1')
        self.chk1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='w')
        
        self.chk2 = customtkinter.CTkCheckBox(self, text='Checkbox 2')
        self.chk2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky='w')

        self.chk3 = customtkinter.CTkCheckBox(self, text='Checkbox 3')
        self.chk3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky='w')

    def get(self) -> list:
        checked = []
        if self.chk1.get() == 1: checked.append(self.chk1.cget('text'))
        if self.chk2.get() == 1: checked.append(self.chk2.cget('text'))
        if self.chk3.get() == 1: checked.append(self.chk3.cget('text'))
        return checked

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title('Using Frames')
        self.geometry('400x250')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.chk_frame = MyCheckBoxFrame(self)
        self.chk_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsw')
        
        self.button = customtkinter.CTkButton(self, text='My Button', command=self.button_callback)
        self.button.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

    def button_callback(self):
        print('Checkeds:', self.chk_frame.get())

app = App()
app.mainloop()

## Dynamic Frames
class MyCheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.checkboxes = []

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=3)
        self.title.grid(row=0, column=0, padx=0, pady=0, sticky='ew')

        for i, val in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=val)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10,0), sticky='w')
            self.checkboxes.append(checkbox)

    def get(self) -> list:
        checked = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked.append(checkbox.cget('text'))
        return checked
    
class MyRadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value='')

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color='gray30', corner_radius=3)
        self.title.grid(row=0, column=0, padx=0, pady=0, sticky='ew')

        for i, val in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=val, value=val, variable=self.variable)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky='w')
            self.radiobuttons.append(radiobutton)

    def get(self):
            return self.variable.get()
        
    def set(self, value):
        self.variable.set(value)    
        
    
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.title('Using Dynamic Frames')
        self.geometry('800x220')
        self.grid_columnconfigure((0,1,2), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.chk_frame1 = MyCheckboxFrame(self, title='Values CHKs', values=['Value 1', 'Value 2', 'Value 3', 'Value 4', 'Value 5', 'Value 6'])
        self.chk_frame1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky='nsew')

        self.chk_frame2 = MyCheckboxFrame(self, title='Options CHKs', values=['Option 1', 'Option 2'])
        self.chk_frame2.grid(row=0, column=1, padx=10, pady=(10, 0), sticky='nsew')
        self.chk_frame2.configure(fg_color='transparent')

        self.rdb_frame1 = MyRadioButtonFrame(self, 'Radios', values=['Radio 1', 'Radio2'])
        self.rdb_frame1.grid(row=0, column=2, padx=10, pady=(10, 0), sticky='nsew')
        
        self.button = customtkinter.CTkButton(self, text='My Button', command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky='ew', columnspan=3)

    def button_callback(self):
        print('Checkeds:', self.chk_frame1.get())
        print('Checkeds:', self.chk_frame2.get())
        print('Checkeds:', self.rdb_frame1.get())


customtkinter.set_appearance_mode('light')
customtkinter.deactivate_automatic_dpi_awareness()
customtkinter.set_widget_scaling(1.2)
customtkinter.set_window_scaling(1.2)
app = App()
app.mainloop()
