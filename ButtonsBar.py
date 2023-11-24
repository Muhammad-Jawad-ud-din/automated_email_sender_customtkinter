import customtkinter

class ButtonsBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(3, weight=25)
        self.grid_columnconfigure(0, weight=1)

        # add widgets onto the frame
        self.loadExcelBtn = customtkinter.CTkButton(self, text="Load Excel File")
        self.loadDirBtn = customtkinter.CTkButton(self, text="Load Papers Folder")
        self.loadTemplateBtn = customtkinter.CTkButton(self, text="Load Email Tempate")
        
        self.loadExcelBtn.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="n")
        self.loadDirBtn.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="n")
        self.loadTemplateBtn.grid(row=2, column=0, padx=20, pady=(20, 0), sticky="n")
        