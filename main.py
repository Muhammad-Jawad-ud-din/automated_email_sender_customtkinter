import customtkinter
from ButtonsBar import ButtonsBar 
from MiddleFame import MiddleFrame
from FilesFrame import FilesFrame

customtkinter.set_appearance_mode("system")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.geometry(f"{size[0]}x{size[1]}")
        self.title(title)
        # self.resizable(False, False) # User can't change the windows size
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure((0, 1, 2), weight=4)


        
        self.buttonsBar = ButtonsBar(master=self)
        self.buttonsBar.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        
        self.buttonsBar1 = MiddleFrame(master=self)
        self.buttonsBar1.grid(row=0, column=1, ipadx=220, pady=10, sticky="nsew")

        self.buttonsBar2 = FilesFrame(master=self)
        self.buttonsBar2.grid(row=0, column=2, padx=10, pady=10, sticky="nsew")        
        
        # self.buttonsBar = ButtonsBar(master=self)
        # self.buttonsBar.grid(row=0, column=0, padx=(0, 500), sticky="nsew")

               
if __name__ == "__main__":
    app = App("Automated Email Sender", (980, 500))
    app.mainloop()