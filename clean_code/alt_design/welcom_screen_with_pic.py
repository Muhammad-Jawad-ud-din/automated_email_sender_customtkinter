import customtkinter
from PIL import Image
GLOBAL_FONT = "Cascadia Mono" # "Segoe Print" "Constantia"
DESCRIPTION_TEXT = '''Welcome to the Email Sender GUI App! 
This user-friendly tool simplifies email distribution by allowing seamless import of student 
data from Excel and attachment of PDF documents based on student IDs. 
Automate personalized emails, preview before sending, and manage logs effortlessly. 
Ideal for educational institutions and businesses seeking efficient and personalized communication workflows.'''

class WelcomeScreen(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.grid_rowconfigure(0, weight=5)
        self.grid_columnconfigure((0,1), weight=1)

        self.headerFont = customtkinter.CTkFont(family=GLOBAL_FONT, size=30, weight="bold")
        self.descriptionFont = customtkinter.CTkFont(family=GLOBAL_FONT, size=15)
        self.buttonsFont = customtkinter.CTkFont(family=GLOBAL_FONT, size=10)

        self.backgroundImage = customtkinter.CTkImage(Image.open("./background_picture.png"), size=(1000, 450))
        self.backgroundImageLabel = customtkinter.CTkLabel(self, image=self.backgroundImage, text='')

        self.rightFrame = customtkinter.CTkFrame(self)
        self.headerLable = customtkinter.CTkLabel(self.rightFrame, text="Automated Emailer Utility",font=self.headerFont)
        self.descLabel = customtkinter.CTkLabel(self.rightFrame, text=DESCRIPTION_TEXT,font=self.descriptionFont)
        self.resultsBtn = customtkinter.CTkButton(self.rightFrame, text="Results", font=self.buttonsFont)
        self.joiningInstBtn = customtkinter.CTkButton(self.rightFrame, text="Joining Instructions", font=self.buttonsFont)
        
        self.backgroundImageLabel.grid(row=0, column=0, padx=20)
        self.rightFrame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")


        self.rightFrame.grid_rowconfigure((0,1,2), weight=1)
        self.rightFrame.grid_columnconfigure((0,1), weight=1)

        self.headerLable.grid(row=0, column=0, columnspan=2)
        self.descLabel.grid(row=1, column=1, columnspan=2)
        self.resultsBtn.grid(row=2, column=0, sticky="w")
        self.joiningInstBtn.grid(row=2, column=1, sticky="e")
    1
