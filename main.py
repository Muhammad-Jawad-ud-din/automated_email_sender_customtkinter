import customtkinter
from tkinter import messagebox

from welcom_screen import WelcomeScreen
from login_utility import LoginUtility
from emails_utility import EmailsUtility
from results_utility import ResultsUtility

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
# customtkinter.set_appearance_mode("light")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

SCREEN_SIZE = (1080, 500)


class App(customtkinter.CTk):
    def __init__(self, title, size):
        try: 
            super().__init__()
            self.geometry(f"{size[0]}x{size[1]}")
            self.title(title)
            self.resizable(False, False)
            self.grid_rowconfigure(0, weight=1)
            self.grid_columnconfigure(0, weight=1)

            self.session_email_address = ''
            self.mailer = '' 
            self.session_started = False

            self.welcom_screen = WelcomeScreen(self)
            self.welcom_screen.grid(row=0, column=0, sticky="nsew")
            self.eval('tk::PlaceWindow . center')

            self.mainloop()
        except Exception as exception: 
            messagebox.showerror(title="Uh-Oh! Error Occured", message=exception)
            self.destroy()
            
    def navigateToResultsUtility(self, current):        
        try: 
            current.destroy()
            self.resultsUtility = ResultsUtility(self)
            self.resultsUtility.grid(row=0, column=0, sticky="nsew")
        except Exception as exception:
            messagebox.showerror(title="Uh-Oh! Error Occured", message=exception)
            self.destroy()
            
    # def navigateToJoiningInstructionsUitlity(self, current):
    #     print('navigateToJoiningInstructionsUitlity - main(app)')
        
    #     current.destroy()
        # self.joiningInstructionsUtility = JoiningInstUtility(self)
        # self.joiningInstructionsUtility.grid(row=0, column=0, sticky="nsew")

        
    def navigateToMainScreen(self, current):
        try:
            current.destroy()
            self.welcom_screen = WelcomeScreen(self)
            self.welcom_screen.grid(row=0, column=0, sticky="nsew")
        except Exception as exception:
            messagebox.showerror(title="Uh-Oh! Error Occured", message=exception)
            self.destroy()
            
    def navigateToEmailSenderUtility(self, data):
        try: 
            self.withdraw()
            self.session_started = False
            self.logInUtility = LoginUtility(self, (SCREEN_SIZE[0]//2, SCREEN_SIZE[1]//2))
            if self.session_started:
                self.emailsUtility = EmailsUtility(self, SCREEN_SIZE, self.mailer, self.session_email_address, data)
            else: 
                messagebox.showwarning(parent=self, title="Log In Failed", message="You must log in to proceed further")
            self.deiconify()
        except Exception as exception: 
            messagebox.showerror(title="Uh-Oh! Error Occured", message=exception)
            self.destroy()
            
if __name__ == "__main__":
    app = App("Automated Paper(s) Emailer", SCREEN_SIZE)
