import os
import numpy
import pandas
import customtkinter

from tkinter import messagebox
from tkinter import filedialog
from CTkScrollableTable import CTkScrollableTable
from CTkXYScrollableFrame import CTkXYScrollableFrame


PDFS_LIST          = list()
STUDENTS_LIST      = list()
EMAIL_BODY_TEXT    = ''
EMAIL_SUBJECT_TEXT = ''
FONT_FAMILY        = "Cascadia Mono"

class LeftSideBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.pdfFilesFrame = master.pdfFilesFrame # PDFs are listed in this frame on load
        self.studentsDataFrame = master.middleFrame.studentsDataFrame # Student Data From Excel is loaded here
        self.master = master
        self.main = master.master

        self.grid_rowconfigure((0, 1, 2, 3, 5), weight=1)
        self.grid_rowconfigure(4, weight=8)
        self.grid_columnconfigure(0, weight=1)

        # Load PDFs Button 
        # Load Excel File
        # Select Sheet_name appears after the excel is loaded
        # Go to WelcomeScreen
        # Empty row to push the Buttons upwards

        self.loadPDFsBtn = customtkinter.CTkButton(self, font=master.buttonFont, text="Load PDFs", command=self.loadPDFsDir)
        self.clearPDFsBtn = customtkinter.CTkButton(self, font=master.buttonFont, text="Clear PDFs", state="disabled", hover_color="red", command=self.clearPDFsDir)

        self.loadExcelBtn = customtkinter.CTkButton(self, font=master.buttonFont, text="Load Students", command=self.loadStudentsData)
        self.clearStudentsBtn = customtkinter.CTkButton(self, font=master.buttonFont, text="Clear Students", state="disabled", hover_color="red", command=self.clearStudentsData)

        self.backBtn = customtkinter.CTkButton(self, font=master.buttonFont, text="Home Screen", command=self.navigateToWelcomScreen)

        self.loadPDFsBtn.grid(row=0, column=0)
        self.clearPDFsBtn.grid(row=1, column=0)

        self.loadExcelBtn.grid(row=2, column=0)
        self.clearStudentsBtn.grid(row=3, column=0)

        self.backBtn.grid(row=5, column=0)


    def loadPDFsDir(self):
        global PDFS_LIST

        directorypath = filedialog.askdirectory()
        for root, dirs, files in os.walk(directorypath):
            for file in files: 
                if file.endswith('.pdf'):
                    PDFS_LIST.append((file, os.path.join(os.path.abspath(root), file)))
        
        if len(PDFS_LIST) == 0:
            messagebox.showerror(title="Failed", message=f"No PDFs Found In The Selected Folder {root}")
            return

        PDFS_NAMES_LIST = [[file[0]] for file in PDFS_LIST]
        self.filesTable = CTkScrollableTable(self.pdfFilesFrame, row=len(PDFS_NAMES_LIST), column=1, values=PDFS_NAMES_LIST)
        self.filesTable.pack()

        self.loadPDFsBtn.configure(state='disabled')
        self.clearPDFsBtn.configure(state="normal")
        messagebox.showinfo(title="Success", message="PDFs Loaded Successfully. Please Double Check the Loaded PDFs List.")

    def getSheetName(self, sheets):

        def loadSheet():
            if not comboBox.get() in sheets:
                messagebox.showerror(title="Invalid", message="Invalid Sheet Name Provided, Please Select One from the list")
            else:
                self.sheetName = comboBox.get()
                sheetsPopUpWindow.destroy()
        
        def disable_event():
            return
        
        sheetsPopUpWindow = customtkinter.CTkToplevel()
        sheetsPopUpWindow.protocol("WM_DELETE_WINDOW", disable_event)
        sheetsPopUpWindow.grid_rowconfigure((0, 1, 2), weight=1)
        sheetsPopUpWindow.grid_columnconfigure(0, weight=1)

        headerLable = customtkinter.CTkLabel(sheetsPopUpWindow, text="Please Select The Sheet Name", font=self.master.buttonFont)
        comboBox = customtkinter.CTkComboBox(sheetsPopUpWindow, values=sheets, width=250, button_color="#2cc985", border_color="#2cc985", dropdown_hover_color="#2cc985", font=self.master.buttonFont, dropdown_font=self.master.buttonFont)
        loadSheetBtn = customtkinter.CTkButton(sheetsPopUpWindow, text="Load Sheet", font=self.master.buttonFont, command=loadSheet)

        headerLable.grid(row=0, column=0, padx=100, pady=10)
        comboBox.grid(row=1, column=0, padx=100, pady=10)
        loadSheetBtn.grid(row=2, column=0, padx=100, pady=10)
        
        sheetsPopUpWindow.geometry("+%d+%d" % (self.main.winfo_rootx()+50,self.main.winfo_rooty()+50))
        self.main.wait_window(sheetsPopUpWindow)
        
    def loadStudentsData(self):
        global STUDENTS_LIST
        file = filedialog.askopenfile(filetypes=[("Excel files", ".xlsx .xls")])
        excelFile = pandas.ExcelFile(file.name)
        
        self.main.withdraw()
        self.sheetName = ''
        self.getSheetName(excelFile.sheet_names)
        self.main.deiconify()

        excelDataFrame = pandas.read_excel(file.name, self.sheetName)
        columns = excelDataFrame.columns.values.tolist()
        STUDENTS_LIST = excelDataFrame.to_numpy()
        studentsList = numpy.insert(STUDENTS_LIST, 0, columns, axis=0).tolist()

        self.studentsDataTable = CTkScrollableTable(master=self.studentsDataFrame, row=len(studentsList), column=len(studentsList[0]), values=studentsList)
        self.studentsDataTable.pack()

        self.loadExcelBtn.configure(state="disabled")
        self.clearStudentsBtn.configure(state="normal")

        messagebox.showinfo(title="Observe The Data In Tables", message="Excels may hold data in different foramts, please observe the data loaded from excel in the middle table.")

    def clearStudentsData(self):
        # On call it should remove the table from the filesSideBar
        # Should disable the 'Clear PDFs' Button
        # Should enable the "Load PDFs" Button
        status = messagebox.askyesno(title="Clear Students Data", message="Would You Like To Clear The Loaded Studnets Data?")
        if status: 
            self.studentsDataTable.destroy()
            self.clearStudentsBtn.configure(state="disabled")
            self.loadExcelBtn.configure(state="normal")
    
    def clearPDFsDir(self): 
        # On call it should remove the table from the filesSideBar
        # Should disable the 'Clear PDFs' Button
        # Should enable the "Load PDFs" Button
        status = messagebox.askyesno(title="Clear The Laaded PDFs", message="Would You Like To Clear The Loaded PDFs?")
        if status: 
            self.filesTable.destroy()
            self.clearPDFsBtn.configure(state="disabled")
            self.loadPDFsBtn.configure(state="normal")

    def navigateToWelcomScreen(self):
        status = messagebox.askokcancel(title="You Sure?", message="Are You Sure to Proceed? Data on This Tab will be lost")
        if status:
            self.master.navigateToWelcomScreen()

class MiddleFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master
        self.textBoxFont = customtkinter.CTkFont(FONT_FAMILY, size=14)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1,2), weight=5)
        self.grid_columnconfigure(0, weight=1)

        # Subject TextArea
        self.subjectTextBox = customtkinter.CTkTextbox(self, font=self.textBoxFont, height=50, border_width=2)
        self.subjectTextBox.grid(row=0, column=0, sticky="nsew")
        self.subjectTextBox.insert("0.0", "Paste The Email Subject Here...")

        # Email Body TextArea
        self.bodyTextBox = customtkinter.CTkTextbox(self, font=self.textBoxFont,  border_width=2)
        self.bodyTextBox.grid(row=1, column=0, pady=5, sticky="nsew")
        self.bodyTextBox.insert("0.0", "Paste The Email Body Content Here...")

        # Excel Loaded Table
        self.studentsDataFrame = CTkXYScrollableFrame(self)
        self.studentsDataFrame.grid(row=2, column=0, sticky="nsew")


class FilesSidebar(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)


class BottomButtonsBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        
        self.master = master

        self.grid_rowconfigure(0, weight=1)
        # self.grid_columnconfigure((1, 2, 3), weight=1)
        # self.grid_columnconfigure(0, weight=10)
        self.grid_columnconfigure(0, weight=1)

        # SendEmails Button
        self.sendEmailsBtn = customtkinter.CTkButton(self, font=self.master.buttonFont, text="Send Emails", command=self.sendEmailsListner)
        self.sendEmailsBtn.grid(row=0, column=0, padx=20, pady=(0, 5), sticky="e")

    def sendEmailsListner(self):
        status = messagebox.askyesno(title="Send Emails?", message="Are You Sure To Proceed To Sender? Did You Double Check The Subject/Body/PDFs/Students Data?")
        if status:
            print("Calling the master navigateToEmailSenderUtility")
            self.master.navigateToEmailSenderUtility()


class ResultsUtility(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.master = master 

        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_columnconfigure(1, weight=20)

        self.buttonFont = customtkinter.CTkFont(family=FONT_FAMILY, size=15)

        # FilesSidebar (pdfFilesFrame is used in LeftSideBar)
        self.pdfFilesFrame = FilesSidebar(self)
        self.pdfFilesFrame.grid(row=0, column=2, ipadx=40, padx=(5,0), pady=5, sticky="nsew")

        # MiddleFrame 
        self.middleFrame = MiddleFrame(self)
        self.middleFrame.grid(row=0, column=1, pady=5, padx=(5, 0), sticky="nsew")
        
        # LeftSideBar
        self.leftSideBar = LeftSideBar(self)
        self.leftSideBar.grid(row=0, column=0, rowspan=2, ipadx=10, sticky="nsew")

        # BottonButtonBar (Buttons not showing)
        self.bottomButtonBar = BottomButtonsBar(self)
        self.bottomButtonBar.grid(row=1, column=1, ipady=20, columnspan=2, sticky="nsew")

    def navigateToWelcomScreen(self):
        self.master.navigateToWelcomScreen(self)

    def navigateToEmailSenderUtility(self):
        global PDFS_LIST
        global STUDENTS_LIST
        global EMAIL_SUBJECT_TEXT 
        global EMAIL_BODY_TEXT 

        # PDFS_NAMES_LIST
        # Studnets Data
        # Subject & Body
        EMAIL_SUBJECT_TEXT = self.middleFrame.subjectTextBox.get("0.0", "end-1c")
        EMAIL_BODY_TEXT = self.middleFrame.bodyTextBox.get("0.0", "end-1c")
        
        print(PDFS_LIST)
        print(STUDENTS_LIST)
        print(EMAIL_SUBJECT_TEXT)
        print(EMAIL_BODY_TEXT)

        # On hold the ResultsUtility
        # Open the emails Utility
        # On Release (Success: ReportUtility)
        pass