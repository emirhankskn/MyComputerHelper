import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("540x960")
        self.title("Örnek Uygulama")
        
        self.grid_rowconfigure(0, weight=1)  
        self.grid_rowconfigure(1, weight=3)  
        self.grid_columnconfigure(0, weight=1)
        
        self.header_frame = customtkinter.CTkFrame(self)
        self.header_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        self.header_frame.grid_rowconfigure(0, weight=1)
        self.header_frame.grid_columnconfigure(0, weight=1)
        
        self.title_label = customtkinter.CTkLabel(self.header_frame, text="Header\nSome Necessaries", font=("Arial", 24), justify="center")
        self.title_label.grid(row=0, column=0, sticky="nsew")
        
        self.button_frame = customtkinter.CTkFrame(self)
        self.button_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)
        
        for i in range(6): self.button_frame.grid_rowconfigure(i, weight=1)
        for j in range(3): self.button_frame.grid_columnconfigure(j, weight=1)
        
        self.btnDownloader = customtkinter.CTkButton(self.button_frame, text="Online Downloader", command=self.openDownloader)
        self.btnDownloader.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        
        self.btnTrimmer = customtkinter.CTkButton(self.button_frame, text="Video/Sound Trimmer", command=self.openTrimmer)
        self.btnTrimmer.grid(row=0, column=1, padx=5, pady=5, sticky="nsew")
        
        self.btnWallet = customtkinter.CTkButton(self.button_frame, text="Wallet", command=self.openWallet)
        self.btnWallet.grid(row=0, column=2, padx=5, pady=5, sticky="nsew")
        
        self.btnFileFormatChanger = customtkinter.CTkButton(self.button_frame, text="File Format Changer", command=self.openFormatChanger)
        self.btnFileFormatChanger.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")
        
        self.btnExample1 = customtkinter.CTkButton(self.button_frame, text="Example 1")
        self.btnExample1.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")
        
        self.btnExample2 = customtkinter.CTkButton(self.button_frame, text="Example 2")
        self.btnExample2.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")
    
    def openDownloader(self): pass    
    def openTrimmer(self): pass
    def openWallet(self): pass
    def openFormatChanger(self):pass

