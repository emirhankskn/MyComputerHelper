import customtkinter as ctk
from abc import ABC, abstractmethod

class BaseMenuFrame(ABC, ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)  # Ana sütun genişlesin
        self.grid_rowconfigure(1, weight=1)     # Alt kısım genişlesin
        self.create_widgets()

    @abstractmethod
    def create_widgets(self): pass

class MenuFrame1(BaseMenuFrame):
    def create_widgets(self):
        self.PADX = 20
        self.PADY = 10
        self.ENTRY_WIDTH = 400

        # URL Bölümü
        self._create_url_entry()
        
        # Format Seçici
        self._create_format_selector()
        
        # Ekstra boşluklar için satır yapılandırması
        self.grid_rowconfigure(2, weight=1)

    def _create_url_entry(self):
        self.url_frame = ctk.CTkFrame(self)
        self.url_frame.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
        self.url_frame.grid_columnconfigure(1, weight=1)
        
        self.url_label = ctk.CTkLabel(self.url_frame, text='URL:')
        self.url_entry = ctk.CTkEntry(
            self.url_frame,
            width=self.ENTRY_WIDTH,
            placeholder_text='Ex: https://www.youtube.com/watch?v=...'
        )
        self.url_label.grid(row=0, column=0, padx=(10,5), pady=self.PADY, sticky='w')
        self.url_entry.grid(row=0, column=1, padx=(0,10), pady=self.PADY, sticky='ew')

    def _create_format_selector(self):
        self.format_var = ctk.StringVar()
        
        self.radio_frame = ctk.CTkFrame(self)
        self.radio_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nsew')
        self.radio_frame.grid_columnconfigure((0,1), weight=1)
        self.radio_frame.grid_rowconfigure(0, weight=1)
        
        self.mp3_radio = ctk.CTkRadioButton(
            self.radio_frame,
            text='MP3',
            variable=self.format_var,
            value='MP3'
        )
        self.mp4_radio = ctk.CTkRadioButton(
            self.radio_frame,
            text='MP4',
            variable=self.format_var,
            value='MP4'
        )
        self.mp3_radio.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        self.mp4_radio.grid(row=0, column=1, padx=10, pady=10, sticky='w')