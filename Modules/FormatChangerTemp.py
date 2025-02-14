import customtkinter as ctk
from Modules import AbstractBase

class FormatChanger(AbstractBase.BaseMenuFrame):
    def create_widgets(self):
        self.PADX = 20
        self.PADY = 10
        self.ENTRY_WIDTH = 400

        self._create_image_frame()
        self._create_image_dragger()
        self._create_document_frame()
        self._create_media_frame()
        self._create_zipping_frame()

    def _create_image_frame(self):
        self._create_comboboxes(row=0, values=['JPEG', 'PNG', 'WEBM', 'BMP'], label_value='Image Format: ')

    def _create_image_dragger(self):
        self._create_drag_drop(row=1)

    def _create_document_frame(self):
        self._create_comboboxes(row=2, values=['PDF', 'DOCX', 'TXT'], label_value='Document Format: ')

    def _create_media_frame(self):
        self._create_comboboxes(row=3, values=['MP3', 'WAV', 'MP4', 'AVI'], label_value='Media Format: ')

    def _create_zipping_frame(self):
        self._create_comboboxes(row=4, values=['RAR', 'ZIP', '7z'], label_value='Compact Format: ')

    def _create_comboboxes(self, row, values, label_value):
        self.frame = ctk.CTkFrame(self)
        self.frame.grid(row=row, column=0, padx=5, pady=5, sticky='new')
        self.grid_columnconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self.frame, text=label_value)
        self.combobox = ctk.CTkComboBox(self.frame, values=values)
        self.label.grid(row=0, column=0, padx=10, pady=7, sticky='w')
        self.combobox.grid(row=0, column=1, padx=10, pady=7, sticky='ew')

        self.labelto = ctk.CTkLabel(self.frame, text='TO')
        self.comboboxto = ctk.CTkComboBox(self.frame, values=values)
        self.labelto.grid(row=0, column=2, padx=10, pady=7, sticky='w')
        self.comboboxto.grid(row=0, column=3, padx=10, pady=7, sticky='ew')

    def _create_drag_drop(self, row):
        self.upload_frame = ctk.CTkFrame(self)
        self.upload_frame.grid(row=row, column=0, padx=5, pady=5, sticky='new')
        self.upload_frame.grid_columnconfigure(0, weight=1)