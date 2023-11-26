import customtkinter

GLOBAL_FONT = "Cascadia Mono" # "Segoe Print" "Constantia"
DESCRIPTION_TEXT = '''Welcome to the Email Sender GUI App! 
This user-friendly tool simplifies email distribution by allowing seamless import of student 
data from Excel and attachment of PDF documents based on student IDs. 
Automate personalized emails, preview before sending, and manage logs effortlessly. 
Ideal for educational institutions and businesses seeking efficient and personalized communication workflows.'''

class WelcomeScreen(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.grid_rowconfigure((0,1,2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.headerFont = customtkinter.CTkFont(family=GLOBAL_FONT, size=30, weight="bold")
        self.descriptionFont = customtkinter.CTkFont(family=GLOBAL_FONT, size=15)

        self.headerLable = customtkinter.CTkLabel(self, 
                                                  text="Automated Emailer Utility",
                                                  font=self.headerFont)
        self.descriptionText = customtkinter.CTkLabel(self, 
                                                      text=DESCRIPTION_TEXT,
                                                      font=self.descriptionFont, 
                                                      compound="center")
        self.multiFilesSender = customtkinter.CTkButton(self, text="Students Results Utility")
        self.singleFileSender = customtkinter.CTkButton(self, text="Joining Intructions Utility")
        self.headerLable.grid(row=1, column=0, columnspan=2, stick="nsew")
        self.descriptionText.grid(row=2, column=0, columnspan=2, stick="nsew")
        self.multiFilesSender.grid(row=3, column=1, sticky="nsew")
        self.singleFileSender.grid(row=3, column=0, sticky="nsew")