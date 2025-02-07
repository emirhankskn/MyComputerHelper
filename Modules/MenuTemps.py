import customtkinter as ctk
from abc import ABC, abstractmethod
from pytube import YouTube
import yt_dlp
from pydub import AudioSegment
from PIL import Image
import requests
from io import BytesIO
import os
import threading

class BaseMenuFrame(ABC, ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.create_widgets()

    @abstractmethod
    def create_widgets(self): pass

class VideoDownloader(BaseMenuFrame):
    def create_widgets(self):
        self.PADX = 20
        self.PADY = 10
        self.ENTRY_WIDTH = 400

        self._create_url_entry()
        self._create_format_selector()
        self._create_quality_selector()
        self._create_video_preview()
        self._create_progress_bar()
        self._create_download_button()
        
    def _create_url_entry(self):
        self.url_frame = ctk.CTkFrame(self)
        self.url_frame.grid(row=0, column=0, padx=5, pady=5, sticky='ew', columnspan=2)
        self.url_frame.grid_columnconfigure(1, weight=1)
        
        self.url_label = ctk.CTkLabel(self.url_frame, text='URL:')

        self.entry_var = ctk.StringVar()
        self.entry_var.trace_add("write", self.fetch_image_from_url)
        self.url_entry = ctk.CTkEntry(
            self.url_frame,
            textvariable=self.entry_var,
            width=self.ENTRY_WIDTH,
            placeholder_text='Ex: https://www.youtube.com/watch?v=...'
        )
        self.url_label.grid(row=0, column=0, padx=(10,5), pady=self.PADY, sticky='w')
        self.url_entry.grid(row=0, column=1, padx=(0,10), pady=self.PADY, sticky='ew')

    def fetch_image_from_url(self, *args):
        url = self.entry_var.get()
        if 'youtube.com/' in url or 'youtu.be/' in url:
            try:
                ydl = yt_dlp.YoutubeDL({'quiet':True})
                info = ydl.extract_info(url, download=False)
                img_url = info.get('thumbnail')
                print(img_url)
                img_data = requests.get(img_url).content
                image = Image.open(BytesIO(img_data)).resize((350, 180))
                self.thumbnail_ctk = ctk.CTkImage(light_image=image, dark_image=image, size=(350, 180))
                self.thumbnail_label.configure(image=self.thumbnail_ctk, text='')            
            except Exception as e:
                self.thumbnail_label.configure(text='Invalid URL')
                print(e)
        else:
            self.thumbnail_label.configure(text='Enter a valid YouTube URL')

    def _create_format_selector(self):
        self.format_var = ctk.StringVar()
        self.format_var.trace_add('write', self._toggle_quality_selector)

        self.radio_frame = ctk.CTkFrame(self)
        self.radio_frame.grid(row=1, column=0, padx=5, pady=5, sticky='nw')
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
        self.mp3_radio.grid(row=0, column=0, padx=5, pady=10, sticky='w')
        self.mp4_radio.grid(row=0, column=1, padx=5, pady=10, sticky='w')

    def _create_quality_selector(self):
        self.quality_combobox_frame = ctk.CTkFrame(self)
        self.quality_combobox_frame.grid(row=1, column=1, padx=5, pady=5, sticky='nw')
        self.quality_combobox_frame.grid_columnconfigure(0, weight=1)
        
        self.quality_label = ctk.CTkLabel(self.quality_combobox_frame, text="Quality:")
        self.quality_combobox = ctk.CTkComboBox(
            self.quality_combobox_frame,
            values=['480p', '720p', '1080p'],
            state='disabled'
        )
        self.quality_label.grid(row=0, column=0, padx=10, pady=7, sticky='w')
        self.quality_combobox.grid(row=0, column=1, padx=10, pady=7, sticky='ew')

    def _toggle_quality_selector(self, *args):
        selected_format = self.format_var.get()
        if selected_format == 'MP4':
            self.quality_combobox.configure(state='normal')
            self.quality_combobox.set('1080p')
        else: self.quality_combobox.configure(state='disabled')

    def _create_video_preview(self):
        self.video_preview_frame = ctk.CTkFrame(self)
        self.video_preview_frame.grid(row=2, column=0, padx=5, pady=5, sticky='nsew', columnspan=2)
        self.video_preview_frame.grid_columnconfigure(0, weight=1)

        self.thumbnail_label = ctk.CTkLabel(self.video_preview_frame, text="URL Waiting...")
        self.thumbnail_label.grid(row=0, column=0, padx=5, pady=5, sticky='nsew', columnspan=2)
    
    def _create_progress_bar(self):
        self.progress_bar_frame = ctk.CTkFrame(self)
        self.progress_bar_frame.grid(row=3, column=0, padx=5, pady=5, stick='ew', columnspan=2)
        self.progress_bar_frame.grid_columnconfigure(0, weight=1)

        self.progress_bar = ctk.CTkProgressBar(self.progress_bar_frame, orientation='horizontal')
        self.progress_bar.grid(row=0, column=0, padx=5, pady=5, sticky='ew', columnspan=2)


    def _create_download_button(self):
        self.download_button_frame = ctk.CTkFrame(self)
        self.download_button_frame.grid(row=4, column=0, padx=5, pady=5, sticky='new', columnspan=2)
        self.download_button_frame.grid_columnconfigure(0, weight=1)
        
        self.download_button = ctk.CTkButton(self.download_button_frame, text='Download Media', command=self.download_media)
        self.download_button.grid(row=0, column=0, padx=5, pady=5, sticky='ew', columnspan=2)

    def download_media(self):
        threading.Thread(target=self._download, daemon=True).start()

    def _download(self):
        url = self.entry_var.get()
        format_type = self.format_var.get()
        quality = self.quality_combobox.get()

        options = {
            'format': 'bestaudio' if format_type == 'MP3' else f'bestvideo[height<={quality.replace('p','')}]+bestaudio/best',
            'merge_output_format': 'mkv',  
            'outtmpl': 'downloads/%(title)s.%(ext)s', 
            'progress_hooks': [self.on_progress],
            'cookies_from_browser': ('brave',),  
        }
        
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

    def on_progress(self, d):
        if d['status'] == 'downloading':
            total_bytes = d.get('total_bytes') or d.get('total_bytes_estimate')
            downloaded_bytes = d.get('downloaded_bytes', 0)
            if total_bytes:
                progress = downloaded_bytes / total_bytes
                self.progress_bar.set(progress)
        elif d['status'] == 'finished':
            self.progress_bar.set(1.0)
            print('Download Completed')


            