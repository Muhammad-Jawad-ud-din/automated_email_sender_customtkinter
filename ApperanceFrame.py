# This calls is not ready for use
import customtkinter

class ApperanceFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.appearanceLabel = customtkinter.CTkLabel(self, text="Apperance Mode")
        self.apperanceBtn = customtkinter.CTkComboBox(self, values=["light", "dark", "system"], command=self.changeApperance)
        self.themeBtn = customtkinter.CTkComboBox(self, values=["blue", "dark-blue", "green"], command=self.changeTheme)
        self.appearanceLabel.grid(row=3, column=0, padx=40, pady=20, sticky="sew")
        self.apperanceBtn.grid(row=4, column=0)
        self.themeBtn.grid(row=5, column=0)
        self.themeBtn.set('blue')
        self.apperanceBtn.set('system')

    def changeApperance(self, mode):
        if mode in ["dark", "light", "system"]:
            customtkinter.set_appearance_mode(mode)
               
    def changeTheme(self, themeColor):
        if themeColor in ["dark-blue", "blue", "green"]:
            customtkinter.set_default_color_theme(themeColor)