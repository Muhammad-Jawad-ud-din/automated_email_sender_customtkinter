import customtkinter
from ButtonsBar import ButtonsBar 
from MiddleFame import MiddleFrame
from FilesFrame import FilesFrame

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.geometry(f"{size[0]}x{size[1]}")
        self.title(title)
        self.resizable(False, False) # User can't change the windows size
        self.grid_rowconfigure(0, weight=10)  # configure grid system
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 1, 2), weight=1)

        
        self.buttonsBar = ButtonsBar(master=self)
        self.buttonsBar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        self.middleFrame = MiddleFrame(master=self)
        self.middleFrame.grid(row=0, column=1, ipadx=150, pady=10, sticky="nsew")
        self.buttonsBar.tabularView = self.middleFrame.tabularView
        self.buttonsBar.tempateArea = self.middleFrame.tempateArea

        self.filesFrame = FilesFrame(master=self)
        self.filesFrame.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")        
        self.buttonsBar.filesFrame = self.filesFrame; 
        
        self.startBtn = customtkinter.CTkButton(self, text="Send Emails", width=90)
        self.startBtn.grid(row=1, column=2 , padx=(0, 20), pady=(0, 10), sticky="e")

        self.clearBtn = customtkinter.CTkButton(self, text="Clear Lists", width=90, fg_color="gray", hover_color="red")
        self.clearBtn.grid(row=1, column=2, padx=(20, 0), pady=(0, 10), sticky="w")

    
if __name__ == "__main__":
    app = App("Automated Email Sender", (980, 500))
    app.mainloop()