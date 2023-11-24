import customtkinter

class ButtonsBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # add widgets onto the frame
        self.loadExcelBtn = customtkinter.CTkButton(self, text="Load Excel File")
        self.loadDirBtn = customtkinter.CTkButton(self, text="Load Papers Folder")
        self.loadTemplateBtn = customtkinter.CTkButton(self, text="Load Email Tempate")
        
        self.loadExcelBtn.grid(row=0, column=0, padx=20, pady=10, sticky="n")
        self.loadDirBtn.grid(row=0, column=0, padx=20, pady=55, sticky="n")
        self.loadTemplateBtn.grid(row=0, column=0, padx=20, pady=100, sticky="n")
        

        # self.appearanceLabel = customtkinter.CTkLabel(self, text="Apperance Mode")
        # self.apperanceBtn = customtkinter.CTkComboBox(self, values=["light", "dark", "system"], command=self.changeApperance)
        # self.themeBtn = customtkinter.CTkComboBox(self, values=["blue", "dark-blue", "green"], command=self.changeTheme)
        # self.appearanceLabel.grid(row=3, column=0, padx=40, pady=20, sticky="sew")
        # self.apperanceBtn.grid(row=4, column=0)
        # self.themeBtn.grid(row=5, column=0)
        # self.themeBtn.set('blue')
        # self.apperanceBtn.set('system')