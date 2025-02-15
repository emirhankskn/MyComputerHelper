import customtkinter as ctk
from tkinter import filedialog
import os
from PIL import Image
import threading
from Modules import AbstractBase

class FormatChanger(AbstractBase.BaseMenuFrame):
    def create_widgets(self):
        self.PADX = 20
        self.PADY = 10
        self.ENTRY_WIDTH = 400
        
        self.selected_files = []
        self.output_format = ctk.StringVar(value="PNG")
        self.output_path = ctk.StringVar(value="Output path not selected.")

        self.create_file_selection_section()
        self.create_format_selection_section()
        self.create_output_section()
        self.create_progress_bar()
        self.create_action_buttons()
        self.create_log_area()

    def create_file_selection_section(self):
        self.lbl_files = ctk.CTkLabel(self, text="Seçilen Dosyalar:")
        self.lbl_files.pack(anchor="w", padx=self.PADX, pady=(20,0))
        
        self.btn_select = ctk.CTkButton(
            self,
            text="Dosya Seç (Ctrl+O)",
            command=self.select_files,
            width=150
        )
        self.btn_select.pack(anchor="w", padx=self.PADX, pady=self.PADY)
        
        self.lbl_selected = ctk.CTkLabel(self, text="Henüz dosya seçilmedi")
        self.lbl_selected.pack(anchor="w", padx=self.PADX)

    def create_format_selection_section(self):
        self.lbl_format = ctk.CTkLabel(self, text="Hedef Format:")
        self.lbl_format.pack(anchor="w", padx=self.PADX, pady=(20,0))
        
        self.combo_format = ctk.CTkComboBox(
            self,
            values=["PNG", "JPEG", "WEBP", "BMP"],
            variable=self.output_format,
            width=150
        )
        self.combo_format.pack(anchor="w", padx=self.PADX, pady=self.PADY)

    def create_output_section(self):
        self.lbl_output = ctk.CTkLabel(self, text="Kayıt Konumu:")
        self.lbl_output.pack(anchor="w", padx=self.PADX, pady=(20,0))
        
        self.btn_output = ctk.CTkButton(
            self,
            text="Klasör Seç",
            command=self.select_output_folder,
            width=150
        )
        self.btn_output.pack(anchor="w", padx=self.PADX, pady=self.PADY)
        
        self.lbl_output_path = ctk.CTkLabel(self, textvariable=self.output_path)
        self.lbl_output_path.pack(anchor="w", padx=self.PADX)

    def create_progress_bar(self):
        self.progress = ctk.CTkProgressBar(self, width=self.ENTRY_WIDTH)
        self.progress.pack(padx=self.PADX, pady=(20,0))
        self.progress.set(0)

    def create_action_buttons(self):
        self.btn_convert = ctk.CTkButton(
            self,
            text="Dönüştür (Ctrl+Enter)",
            command=self.start_conversion_thread,
            fg_color="#2AA876",
            hover_color="#207A5A"
        )
        self.btn_convert.pack(pady=(20,10))

    def create_log_area(self):
        self.txt_log = ctk.CTkTextbox(self, width=600, height=150)
        self.txt_log.pack(padx=self.PADX, pady=(10,20))
        self.txt_log.insert("0.0", "Hazır\n")

    def select_files(self):
        files = filedialog.askopenfilenames(
            title="Dosya Seçin",
            filetypes=[("Image Files", "*.png *.jpg *.jpeg *.webp *.bmp")]
        )
        if files:
            self.selected_files = files
            self.lbl_selected.configure(text=f"{len(files)} dosya seçildi")
            self.add_log(f"{len(files)} dosya seçildi")

    def select_output_folder(self):
        folder = filedialog.askdirectory(title="Kayıt Klasörü Seçin")
        if folder:
            self.output_path.set(folder)
            self.add_log(f"Kayıt yolu: {folder}")

    def start_conversion_thread(self):
        if not self.selected_files:
            self.add_log("Hata: Önce dosya seçin!", is_error=True)
            return
            
        threading.Thread(target=self.convert_files).start()

    def convert_files(self):
        try:
            total_files = len(self.selected_files)
            output_folder = self.output_path.get() if self.output_path.get() != "Kayıt Yolu Seçilmedi" else os.getcwd()
            
            for i, file_path in enumerate(self.selected_files):
                try:
                    self.progress.set(i/total_files)
                    self.update_idletasks()
                    
                    img = Image.open(file_path)
                    base_name = os.path.splitext(os.path.basename(file_path))[0]
                    output_file = os.path.join(
                        output_folder,
                        f"{base_name}_converted.{self.output_format.get().lower()}"
                    )
                    
                    if self.output_format.get() == "JPEG":
                        img = img.convert("RGB")
                        img.save(output_file, quality=95)
                    else:
                        img.save(output_file)
                    
                    self.add_log(f"Başarılı: {os.path.basename(output_file)}")
                except Exception as e:
                    self.add_log(f"Hata ({os.path.basename(file_path)}): {str(e)}", is_error=True)
            
            self.progress.set(1)
            self.add_log("Tüm dönüşümler tamamlandı!")
            
        except Exception as e:
            self.add_log(f"Kritik Hata: {str(e)}", is_error=True)

    def add_log(self, message, is_error=False):
        tag = "error" if is_error else "info"
        self.txt_log.insert("end", message + "\n", tag)
        self.txt_log.see("end")
        self.txt_log.tag_config("error", foreground="#FF5555")
        self.txt_log.tag_config("info", foreground="#CCCCCC")

# Kullanım örneği
if __name__ == "__main__":
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    
    app = ctk.CTk()
    converter = FormatChanger(app)
    converter.pack(fill="both", expand=True)
    app.mainloop()