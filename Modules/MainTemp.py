import customtkinter as ctk
from Modules.VideoDownloaderTemp import VideoDownloader
from Modules.FormatChangerTemp import FormatChanger

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Computer Tools by Keskin')
        self.geometry('600x410')
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.main_frame = MainFrame(self)
        self.main_frame.grid(row=0, column=0, sticky='nsew')

class MainFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.button_panel = ButtonPanel(self, 6, self.switch_content)
        self.button_panel.grid(row=0, column=0, sticky='ns')
        
        self.content_area = ContentArea(self)
        self.content_area.grid(row=0, column=1, sticky='nsew', padx=5, pady=5)

    def switch_content(self, menu_index):
        self.content_area.show_menu(menu_index)

class ButtonPanel(ctk.CTkFrame):
    def __init__(self, master, count, switch_callback):
        super().__init__(master)
        self.count = count
        self.switch_frame = switch_callback
        self.grid_rowconfigure(tuple(range(count)), weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.create_buttons()
        
    def create_buttons(self):
        button_labels = ['Video Downloader', 'Format Changer', 'System Vitals', 'Web Scraper', 'EX', 'EX2']
        for i in range(self.count):
            btn = ctk.CTkButton(
                self, 
                text=button_labels[i], 
                command=lambda idx=i: self.switch_frame(idx),
                anchor="w"  # Metni sola hizala
            )
            btn.grid(row=i, column=0, padx=5, pady=2, sticky='nsew')


class ContentArea(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.current_menu = None
        self.menus = [VideoDownloader, FormatChanger]

    def show_menu(self, menu_index):
        if self.current_menu: 
            self.current_menu.destroy()
        self.current_menu = self.menus[menu_index](self)
        self.current_menu.grid(row=0, column=0, sticky='nsew')