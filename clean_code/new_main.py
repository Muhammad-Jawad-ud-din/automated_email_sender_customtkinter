import customtkinter
from welcom_screen import WelcomeScreen

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
# customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

class App(customtkinter.CTk):
    def __init__(self, title, size):
        super().__init__()
        self.currentWindow = self

        self.geometry(f"{size[0]}x{size[1]}")
        self.title(title)
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.welcomScreen = WelcomeScreen(self)
        self.welcomScreen.grid(row=0, column=0, sticky="nsew")

        self.currentWindow.mainloop()

    def navigateToResultsUtility(self):
        print('navigateToResultsUtility master')
        self.welcomScreen.destroy()

    def navigateToJoiningInstructionsUitlity(self):
        print('navigateToJoiningInstructionsUitlity master')
        self.welcomScreen.destroy()
        # self.joiningInstructionsUtility = JoiningInstUtility(self)
        


if __name__ == "__main__":
    app = App("Automated Emailer", (980, 500))
    # app.mainloop()