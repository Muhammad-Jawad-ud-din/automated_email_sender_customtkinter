import customtkinter
from welcom_screen import WelcomeScreen

customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self, title, size):
        super().__init__()
        
        self.geometry(f"{size[0]}x{size[1]}")
        self.title(title)
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.welcomScreen = WelcomeScreen(self)
        self.welcomScreen.grid(row=0, column=0, sticky="nsew")
        

if __name__ == "__main__":
    app = App("Automated Emailer", (980, 500))
    app.mainloop()