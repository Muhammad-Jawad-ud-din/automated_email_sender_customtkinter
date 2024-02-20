import customtkinter
from tkinter import messagebox

GLOBAL_FONT = "Cascadia Mono" # "Segoe Print" "Constantia"
DESCRIPTION_TEXT = '''Welcome to the Email Sender GUI App! 
This user-friendly tool simplifies email distribution by allowing seamless import of student 
data from Excel and attachment of PDF documents based on student IDs. 
Automate personalized emails, preview before sending, and manage logs effortlessly. '''

class WelcomeScreen(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        try: 
            super().__init__(master, **kwargs)

            self.master = master 
            self.grid_rowconfigure((0, 1, 2), weight=1)
            self.grid_columnconfigure(0, weight=1)
            
            self.headerFont = customtkinter.CTkFont(family=GLOBAL_FONT, size=30, weight="bold")
            self.descriptionFont = customtkinter.CTkFont(family=GLOBAL_FONT, size=15)
            self.buttonsFont = customtkinter.CTkFont(family=GLOBAL_FONT, size=20)

            self.headerLable = customtkinter.CTkLabel(self, text="Automated Email Sender Utility",font=self.headerFont) 
            self.descriptionText = customtkinter.CTkLabel(self, text=DESCRIPTION_TEXT,font=self.descriptionFont)
            self.buttonsFrame = customtkinter.CTkFrame(self)

            self.buttonsFrame.grid_rowconfigure(0, weight=1)
            self.buttonsFrame.grid_columnconfigure(0, weight=1)

            self.multiFilesSender = customtkinter.CTkButton(self.buttonsFrame, text="Students Results Utility", font=self.buttonsFont   , command=self.navigateToResultsUtility)
            # self.singleFileSender = customtkinter.CTkButton(self.buttonsFrame, text="Joining Intructions Utility", font=self.buttonsFont, command=self.navigateToJoiningInstructionsUitlity)
            
            self.headerLable.grid(row=0, column=0, pady=(20, 0), stick="nsew")
            self.descriptionText.grid(row=1, column=0, stick="nsew")
            self.buttonsFrame.grid(row=2, column=0, padx=20, pady=20, stick="nsew")
            
            self.multiFilesSender.grid(row=0, column=0, padx=200, pady=40, sticky="nsew")
            # self.singleFileSender.grid(row=0, column=1, padx=40, pady=40, sticky="nsew")
        except Exception as exception: 
            messagebox.showerror(title="Uh-Oh! Error Occured", message=exception)
            self.destroy()
            
            
    def navigateToResultsUtility(self):
        try: 
            self.master.navigateToResultsUtility(self)
        except Exception as exception: 
            messagebox.showerror(title="Uh-Oh! Error Occured", message=exception)
            self.destroy()
            
            
    # def navigateToJoiningInstructionsUitlity(self):
    #     self.master.navigateToJoiningInstructionsUitlity(self)