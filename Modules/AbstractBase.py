from abc import ABC, abstractmethod
import customtkinter as ctk

class BaseMenuFrame(ABC, ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.create_widgets()
    @abstractmethod
    def create_widgets(self): pass