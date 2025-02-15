import customtkinter as ctk
from tkinter import filedialog
import os
from PIL import Image
import threading
from Modules import AbstractBase

class FormatChanger(AbstractBase.BaseMenuFrame):
    def create_widgets(self):
        self.selected_files = []
        self._image_formats = ['JPEG', 'PNG', 'WEBP', 'BMP']
        self._document_formats = ['PDF', 'DOCX', 'TXT']
        self._media_formats = ['MP3', 'MP4', 'WAV', 'AVI', 'WEBM', 'MKV']
        self._zipping_formats = ['ZIP', 'RAR', '7z']

        self.output_format = ctk.StringVar(value='PNG')
        self.output_path = ctk.StringVar(value='Output path not selected.')

        self._create_file_selection()
        self._create_format_selection()
        self._create_output_frame()
        self._create_action_button()
        self._create_log_area()
        self._create_progress_bar()

    def _create_file_selection(self):
        self.file_selection_frame = ctk.CTkFrame(self)
        self.file_selection_frame.grid(row=0, column=0, padx=5, pady=5, sticky='new')

        self.lbl_files = ctk.CTkLabel(self.file_selection_frame, text='Chosen Files:')
        self.lbl_files.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.btn_select = ctk.CTkButton(
            self.file_selection_frame,
            text='Choose File (Ctrl+O)',
            command=self.select_files)
        self.btn_select.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.lbl_selected = ctk.CTkLabel(self.file_selection_frame, text='File not selected yet.')
        self.lbl_selected.grid(row=0, column=2, padx=5, pady=5, sticky='w')

    def _create_format_selection(self):
        self.format_selection_frame = ctk.CTkFrame(self)
        self.format_selection_frame.grid(row=1, column=0, padx=5, pady=5, sticky='new')
        
        self.lbl_format = ctk.CTkLabel(self.format_selection_frame, text='Target Format:')
        self.lbl_format.grid(row=0, column=0, padx=5, pady=5, sticky='w')

        self.cmb_format = ctk.CTkComboBox(
            self.format_selection_frame,
            values=[],
            variable=self.output_format
        )
        self.cmb_format.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self._update_format_combobox()

    def _update_format_combobox(self):
        if not self.selected_files:
            self.cmb_format.configure(values=['Select files first'], state='disabled')
            return
        selected_exts = [os.path.splitext(file)[1].upper().lstrip('.') for file in self.selected_files]

        format_mapping = [
            {
                'name' : 'IMAGE',
                'source' : self._image_formats,
                'target' : self._image_formats
            },
            {
                'name' : 'DOCUMENT',
                'source' : self._document_formats,
                'target' : self._document_formats
            },
            {
                'name' : 'MEDIA',
                'source' : self._media_formats,
                'target' : self._media_formats
            },
            {
                'name' : 'ZIP',
                'source' : self._zipping_formats,
                'target' : self._zipping_formats
            }
        ]        
        current_category = None
        values = list()

        for category in format_mapping:
            if all(ext in category['source'] for ext in selected_exts):
                current_category = category
                values = category['target']
                break

        if current_category:
            self.cmb_format.configure(values=values, state='normal')
            self.output_format.set(values[0] if values else '')
        else:
            self.cmb_format.configure(values=['Mixed Formats!'], state='disabled')
        
    def select_files(self):
        files = filedialog.askopenfilenames(
            title = 'Select File:',
            filetypes=[
                ('Image Files', '*.png *.jpg *.jpeg *.webp *.bmp'),
                ('Document Files', '*.pdf *.docx *.txt'),
                ('Media Files', '*.mp3 *.mp4 *.wav *.avi *.webm *.mkv'),
                ('Zipping Files', '*.rar *.zip *.7z')
            ]
        )
        if files:
            self.selected_files = files
            self.lbl_selected.configure(text=f'{len(files)} file selected.')
            self.add_log(f'{len(files)} file selected.')
            self._update_format_combobox()

    def _create_output_frame(self):
        self.output_frame = ctk.CTkFrame(self)
        self.output_frame.grid(row=2, column=0, padx=5, pady=5, sticky='new')
        
        self.lbl_output = ctk.CTkLabel(self.output_frame, text='Output Path:')
        self.lbl_output.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        
        self.btn_output = ctk.CTkButton(
            self.output_frame, 
            text='Select Directory',
            command=self.select_output_folder)
        self.btn_output.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        self.lbl_output_path = ctk.CTkLabel(self.output_frame, textvariable=self.output_path)
        self.lbl_output_path.grid(row=0, column=2, padx=5, pady=5, sticky='w')

    def select_output_folder(self):
        folder = filedialog.askdirectory(title='Select saving directory')
        if folder:
            self.output_path.set(folder)
            self.add_log(f'Save path: {folder}')

    def _create_action_button(self):
        self.btn_convert_frame = ctk.CTkFrame(self)
        self.btn_convert_frame.grid(row=3, column=0, padx=5, pady=5, sticky='new')
        self.btn_convert_frame.grid_columnconfigure(0, weight=1)
        self.btn_convert = ctk.CTkButton(
            self.btn_convert_frame,
            text='Convert (Ctrl+Enter)',
            command = self.start_conversion_thread,
            fg_color='#2AA876',
            hover_color='#207A5A'
        )
        self.btn_convert.grid(row=0, column=0, padx=5, pady=5, sticky='ew')

    def start_conversion_thread(self):
        if not self.select_files:
            self.add_log('Error: Select file first!', is_error=True)
            return
        threading.Thread(target=self.convert_files).start()

    def convert_files(self):
        pass

    def _create_log_area(self):
        self.log_area_frame = ctk.CTkFrame(self)
        self.log_area_frame.grid(row=4, column=0, padx=5, pady=5, sticky='new')
        self.txt_log = ctk.CTkTextbox(self.log_area_frame, width=600, height=150)
        self.txt_log.grid(row=0, column=0, padx=5, pady=5)
        self.txt_log.insert('0.0', 'Ready\n')
    
    def _create_progress_bar(self):
        self.progress_bar_frame = ctk.CTkFrame(self)
        self.progress_bar_frame.grid(row=5, column=0, padx=5, pady=5, sticky='new')
        self.progress_bar_frame.grid_columnconfigure(0, weight=1)

        self.progress_bar = ctk.CTkProgressBar(self.progress_bar_frame)
        self.progress_bar.grid(row=0, column=0, padx=5, pady=5, sticky='ew')
        self.progress_bar.set(0)

    def add_log(self, str): pass