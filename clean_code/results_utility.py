import os
import customtkinter
from tkinter import filedialog
from CTkScrollableTable import CTkScrollableTable
from CTkXYScrollableFrame import CTkXYScrollableFrame


GLOBAL_FONT = "Cascadia Mono"
PDFS_LIST = list()
PDFS_NAMES_LIST = list()


class LeftSideBar(customtkinter.CTkFrame):
    def __init__(self, master, buttonFont, **kwargs):
        super().__init__(master, **kwargs)
        
        self.filesSidebar = master.filesSidebar # PDFs are listed in this frame on load

        self.grid_rowconfigure((0, 1, 2, 3, 5), weight=1)
        self.grid_rowconfigure(4, weight=8)
        self.grid_columnconfigure(0, weight=1)

        # Load PDFs Button 
        # Load Excel File
        # Select Sheet_name appears after the excel is loaded
        # Go to WelcomeScreen
        # Empty row to push the Buttons upwards

        self.loadPDFsBtn = customtkinter.CTkButton(self, font=buttonFont, text="Load PDFs", command=self.loadPDFsDir)
        self.clearTablesBtn = customtkinter.CTkButton(self, font=buttonFont, text="Clear PDFs", state="disabled", fg_color="gray", hover_color="red")

        self.loadExcelBtn = customtkinter.CTkButton(self, font=buttonFont, text="Load Students", command=self.loadExcelFile)
        self.clearStudentsBtn = customtkinter.CTkButton(self, font=buttonFont, text="Clear Students", state="disabled", fg_color="gray", hover_color="red")

        self.backBtn = customtkinter.CTkButton(self, font=buttonFont, text="Home Screen", command=self.naviageToWelcomeScreen)

        self.loadPDFsBtn.grid(row=0, column=0)
        self.clearTablesBtn.grid(row=1, column=0)

        self.loadExcelBtn.grid(row=2, column=0)
        self.clearStudentsBtn.grid(row=3, column=0)

        self.backBtn.grid(row=5, column=0)


    def loadPDFsDir(self):
        directorypath = filedialog.askdirectory()

        print('Selected:', directorypath)
        for root, dirs, files in os.walk(directorypath):
            for file in files: 
                if file.endswith('.pdf'):
                    PDFS_LIST.append((file, os.path.join(os.path.abspath(root), file)))

        PDFS_NAMES_LIST = [[file[0]] for file in PDFS_LIST]
        print(PDFS_NAMES_LIST)
        table = CTkScrollableTable(self.filesSidebar, row=len(PDFS_NAMES_LIST), column=1, values=PDFS_NAMES_LIST)
        table.pack()
        self.loadPDFsBtn.configure(state='disabled')

    def loadExcelFile(self):
        pass

    def naviageToWelcomeScreen(self):
        pass

class MiddleFrame(customtkinter.CTkFrame):
    def __init__(self, master, buttonFont, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1,2), weight=5)
        self.grid_columnconfigure(0, weight=1)

        # Subject TextArea
        self.subjectTextBox = customtkinter.CTkTextbox(self, font=customtkinter.CTkFont(GLOBAL_FONT, size=14), height=50, border_width=2)
        self.subjectTextBox.grid(row=0, column=0, sticky="nsew")
        self.subjectTextBox.insert("0.0", "Paste The Email Subject Here...")

        # Email Body TextArea
        self.bodyTextBox = customtkinter.CTkTextbox(self, font=customtkinter.CTkFont(GLOBAL_FONT, size=14),  border_width=2)
        self.bodyTextBox.grid(row=1, column=0, pady=5, sticky="nsew")
        self.bodyTextBox.insert("0.0", "Paste The Email Body Content Here...")

        # Excel Loaded Table
        self.excelTableFrame = CTkXYScrollableFrame(self)
        self.excelTableFrame.grid(row=2, column=0, sticky="nsew")


class FilesSidebar(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)



class BottomButtonsBar(customtkinter.CTkFrame):
    def __init__(self, master, buttonFont, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((1, 2, 3), weight=1)
        self.grid_columnconfigure(0, weight=10)

        # Empty Column to push buttons to right 
        # ClearTables Button 
        # self.clearTablesBtn = customtkinter.CTkButton(self, font=buttonFont, text="Clear Students", fg_color="gray", hover_color="red")
        # self.clearTablesBtn.grid(row=0, column=1)

        # self.clearTablesBtn = customtkinter.CTkButton(self, font=buttonFont, text="Clear PDFs", fg_color="gray", hover_color="red")
        # self.clearTablesBtn.grid(row=0, column=2)

        # SendEmails Button
        self.sendEmailsBtn = customtkinter.CTkButton(self, font=buttonFont, text="Send Emails")
        self.sendEmailsBtn.grid(row=0, column=3)


class ResultsUtility(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_columnconfigure(1, weight=20)

        self.buttonFont = customtkinter.CTkFont(family=GLOBAL_FONT, size=15)

        # FilesSidebar (filesSidebar is used in LeftSideBar)
        self.filesSidebar = FilesSidebar(self)
        self.filesSidebar.grid(row=0, column=2, ipadx=40, padx=(5,0), pady=5, sticky="nsew")

        # LeftSideBar
        self.leftSideBar = LeftSideBar(self, self.buttonFont)
        self.leftSideBar.grid(row=0, column=0, rowspan=2, ipadx=10, padx=(0,5), sticky="nsew")

        # MiddleFrame 
        self.middleFrame = MiddleFrame(self, self.buttonFont)
        self.middleFrame.grid(row=0, column=1, pady=5, sticky="nsew")

        # BottonButtonBar (Buttons not showing)
        self.bottomButtonBar = BottomButtonsBar(self, self.buttonFont)
        self.bottomButtonBar.grid(row=1, column=1, ipady=20, columnspan=2, sticky="nsew")

