import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Modular Window')
        self.geometry('960x540')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_frame = MainFrame(self)
        self.main_frame.grid(row=0, column=0, sticky='nsew')

class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=8)
        self.grid_rowconfigure(0, weight=1)

        self.button_panel = ButtonPanel(self, self.switch_content)
        self.content_area = ContentArea(self)

        self.button_panel.grid(row=0, column=0, sticky='nsew')
        self.content_area.grid(row=0, column=1, sticky='nsew')

    def switch_content(self, menu_index):
        self.content_area.show_menu(menu_index)


class ButtonPanel(ctk.CTkFrame):
    def __init__(self, master, switch_callback):
        super().__init__(master)
        self.switch_frame = switch_callback
        self.create_buttons()

    def create_buttons(self):
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
            btn = ctk.CTkButton(self, text=f"Unit {i+1}", command=lambda idx=i : self.switch_frame(idx))
            btn.grid(row=i, column=0, padx=10, pady=10, sticky='nsew')


class ContentArea(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.current_menu = None
        self.menus = [MenuFrame1, MenuFrame2, MenuFrame3, MenuFrame4]

    def show_menu(self, menu_index):
        if self.current_menu:
            self.current_menu.destroy()
        self.current_menu = self.menus[menu_index](self)
        self.current_menu.grid(row=0, column=0, sticky='nsew')

class BaseMenuFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.create_widgets()

    def create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

class MenuFrame1(BaseMenuFrame):
    def create_widgets(self):
        super().create_widgets()
        self.label = ctk.CTkLabel(self, text='Menu 1 Content')
        self.textbox = ctk.CTkTextbox(self)
        self.label.grid(row=0, column=0)
        self.textbox.grid(row=1, column=0, sticky='nsew')

class MenuFrame2(BaseMenuFrame):
    def create_widgets(self):
        super().create_widgets()
        self.label = ctk.CTkLabel(self, text='Menu 2 Content')
        self.textbox = ctk.CTkTextbox(self)
        self.label.grid(row=0, column=0)
        self.textbox.grid(row=1, column=0, sticky='nsew')

class MenuFrame3(BaseMenuFrame):
    def create_widgets(self):
        super().create_widgets()
        self.label = ctk.CTkLabel(self, text='Menu 3 Content')
        self.textbox = ctk.CTkTextbox(self)
        self.label.grid(row=0, column=0)
        self.textbox.grid(row=1, column=0, sticky='nsew')

class MenuFrame4(BaseMenuFrame):
    def create_widgets(self):
        super().create_widgets()
        self.label = ctk.CTkLabel(self, text='Menu 4 Content')
        self.textbox = ctk.CTkTextbox(self)
        self.label.grid(row=0, column=0)
        self.textbox.grid(row=1, column=0, sticky='nsew')