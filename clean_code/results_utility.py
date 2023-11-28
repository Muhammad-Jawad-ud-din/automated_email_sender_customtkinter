import customtkinter
from CTkXYScrollableFrame import CTkXYScrollableFrame

GLOBAL_FONT = "Cascadia Mono"

class LeftSideBar(customtkinter.CTkFrame):
    def __init__(self, master, buttonFont, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_rowconfigure(3, weight=8)
        self.grid_columnconfigure(0, weight=1)

        # Load PDFs Button 
        # Load Excel File
        # Select Sheet_name appears after the excel is loaded
        # Go to WelcomeScreen
        # Empty row to push the Buttons upwards

        self.loadPDFsBtn = customtkinter.CTkButton(self, font=buttonFont, text="Load PDFs")
        self.loadExcelBtn = customtkinter.CTkButton(self, font=buttonFont, text="Load Excel")
        self.backBtn = customtkinter.CTkButton(self, font=buttonFont, text="Home Screen")

        self.loadPDFsBtn.grid(row=0, column=0)
        self.loadExcelBtn.grid(row=1, column=0)
        self.backBtn.grid(row=2, column=0)



class MiddleFrame(customtkinter.CTkFrame):
    def __init__(self, master, buttonFont, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1,2), weight=5)
        self.grid_columnconfigure(0, weight=1)

        # Subject TextArea
        self.subjectTextBox = customtkinter.CTkTextbox(self, font=customtkinter.CTkFont(GLOBAL_FONT, size=14), height=50, border_width=2)
        self.subjectTextBox.grid(row=0, column=0, sticky="nsew")
        
        # Email Body TextArea
        self.bodyTextBox = customtkinter.CTkTextbox(self, font=customtkinter.CTkFont(GLOBAL_FONT, size=14),  border_width=2)
        self.bodyTextBox.grid(row=1, column=0, pady=5, sticky="nsew")

        # Excel Loaded Table
        self.excelTableFrame = CTkXYScrollableFrame(self)
        self.excelTableFrame.grid(row=2, column=0, sticky="nsew")


class RightSideBar(CTkXYScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)



class BottomButtonsBar(customtkinter.CTkFrame):
    def __init__(self, master, buttonFont, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((1,2), weight=1)
        self.grid_columnconfigure(0, weight=20)

        # Empty Column to push buttons to right 
        # ClearTables Button 
        self.clearTablesBtn = customtkinter.CTkButton(self, font=buttonFont, text="Clear Lists", fg_color="gray", hover_color="red")
        self.clearTablesBtn.grid(row=0, column=0, sticky="e")

        # SendEmails Button
        self.sendEmailsBtn = customtkinter.CTkButton(self, font=buttonFont, text="Send Emails")
        self.sendEmailsBtn.grid(row=0, column=1, sticky="e")


class ResultsUtility(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_columnconfigure(1, weight=20)

        self.buttonFont = customtkinter.CTkFont(family=GLOBAL_FONT, size=15)

        # LeftSideBar
        self.leftSideBar = LeftSideBar(self, self.buttonFont)
        self.leftSideBar.grid(row=0, column=0, rowspan=2, ipadx=10, padx=(0,5), sticky="nsew")

        # MiddleFrame 
        self.middleFrame = MiddleFrame(self, self.buttonFont)
        self.middleFrame.grid(row=0, column=1, pady=5, sticky="nsew")

        # RightSideBar
        self.rightSideBar = RightSideBar(self)
        self.rightSideBar.grid(row=0, column=2, padx=(5,0), pady=5, sticky="nsew")

        # BottonButtonBar (Buttons not showing)
        self.bottomButtonBar = BottomButtonsBar(self, self.buttonFont)
        self.bottomButtonBar.grid(row=1, column=1, ipady=20, columnspan=2, sticky="nsew")

