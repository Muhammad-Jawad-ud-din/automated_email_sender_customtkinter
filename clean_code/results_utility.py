import os
import numpy
import pandas
import customtkinter

from tkinter import messagebox
from tkinter import filedialog
from collections import defaultdict
from CTkScrollableTable import CTkScrollableTable
from CTkXYScrollableFrame import CTkXYScrollableFrame


PDFS_LIST          = list()
STUDENTS_LIST      = list()
EMAIL_BODY_TEXT    = ''
EMAIL_SUBJECT_TEXT = ''
FONT_FAMILY        = "Cascadia Mono"
STUDENT_DATA_FRAME = ""


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

        self.backBtn = customtkinter.CTkButton(self, font=master.buttonFont, text="Home Screen", hover_color="red", command=self.navigateToWelcomScreen)

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
            messagebox.showerror(parent=self, title="Failed", message=f"No PDFs Found In The Selected Folder {root}")
            return

        PDFS_NAMES_LIST = [[file[0]] for file in PDFS_LIST]
        self.filesTable = CTkScrollableTable(self.pdfFilesFrame, row=len(PDFS_NAMES_LIST), column=1, values=PDFS_NAMES_LIST)
        self.filesTable.pack()

        self.loadPDFsBtn.configure(state='disabled')
        self.clearPDFsBtn.configure(state="normal")
        messagebox.showinfo(parent=self, title="Success", message="PDFs Loaded Successfully. Please Double Check the Loaded PDFs List.")
        print(PDFS_LIST)
    def getSheetName(self, sheets):
        
        def loadSheet():
            if not comboBox.get() in sheets:
                messagebox.showerror(parent=self, title="Invalid", message="Invalid Sheet Name Provided, Please Select One from the list")
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
        global STUDENT_DATA_FRAME

        def validateExcelData(df):
            # Check if the first column contains numeric values (ID)
            if not pandas.to_numeric(df.iloc[:, 0], errors='coerce').notnull().all():
                messagebox.showerror(parent=self, title="Invalid Student IDs", message="First column should contain only numeric values (ID).")
                return False

            # Check if the fourth column contains valid email addresses
            if not df.iloc[:, 3].astype(str).str.contains('@').all():
                messagebox.showerror(parent=self, title="Invalid Email Addresses", message="Fourth column should contain valid email addresses.")
                return False

            # validate the input excel file
            if df.isnull().values.any():
                messagebox.showerror(parent=self, title="Empty Cells", message="Empty, Null or Undefined values found in the excel, please provide clean data")
                return False

            # Check for duplicate IDs
            duplicate_ids = df[df.duplicated(df.columns[0], keep=False)]
            if not duplicate_ids.empty:
                messagebox.showerror(parent=self, title="Dupilcate IDs", message="Duplicate IDs found:")
                return False

            # Check for duplicate email addresses
            duplicate_emails = df[df.duplicated(df.columns[3], keep=False)]
            if not duplicate_emails.empty:
                messagebox.showerror(parent=self, title="Duplicate Emails", message="Duplicate Email Addresses found:")
                return False

            return True

        file = filedialog.askopenfile(filetypes=[("Excel files", ".xlsx .xls")])
        excelFile = pandas.ExcelFile(file.name)
        
        self.main.withdraw()
        self.sheetName = ''
        self.getSheetName(excelFile.sheet_names)
        self.main.deiconify()

        excelDataFrame = pandas.read_excel(file.name, self.sheetName)
        if validateExcelData(excelDataFrame):
            STUDENT_DATA_FRAME = excelDataFrame.copy()
            STUDENTS_LIST = excelDataFrame.to_numpy()

            columns = excelDataFrame.columns.values.tolist()
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
        status = messagebox.askyesno(parent=self, title="Clear Students Data", message="Would You Like To Clear The Loaded Studnets Data?")
        if status: 
            self.studentsDataTable.destroy()
            self.clearStudentsBtn.configure(state="disabled")
            self.loadExcelBtn.configure(state="normal")
    
    def clearPDFsDir(self): 
        # On call it should remove the table from the filesSideBar
        # Should disable the 'Clear PDFs' Button
        # Should enable the "Load PDFs" Button
        status = messagebox.askyesno(parent=self, title="Clear The Laaded PDFs", message="Would You Like To Clear The Loaded PDFs?")
        if status: 
            self.filesTable.destroy()
            self.clearPDFsBtn.configure(state="disabled")
            self.loadPDFsBtn.configure(state="normal")
            PDFS_LIST = []

    def navigateToWelcomScreen(self):
        status = messagebox.askokcancel(parent=self, title="You Sure?", message="Are You Sure to Proceed? Data on This Tab will be lost")
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

        def formatData(papers, students, subject, body):
            studentsDataWithPapers = defaultdict(lambda: {'email_address': '', 'first_name': '', 'full_name': '', 'papers': [], 'subject': '', 'email_body': ''})

            for studentId, surname, fullname, email in students:
                studentsDataWithPapers[studentId]['email_address'] = email
                studentsDataWithPapers[studentId]['first_name'] = surname
                studentsDataWithPapers[studentId]['full_name'] = fullname
                studentsDataWithPapers[studentId]['subject'] = subject
                studentsDataWithPapers[studentId]['email_body'] = body
                
                for paper_name, paper_path in papers:
                    if str(studentId) in paper_name:        
                        studentsDataWithPapers[studentId]['papers'].append((paper_name, paper_path))

            return studentsDataWithPapers
        
        status = messagebox.askyesno(parent=self, title="Send Emails?", message="Are You Sure To Proceed To Sender? Did You Double Check The Subject/Body/PDFs/Students Data?")
        if status:
            global PDFS_LIST
            global STUDENTS_LIST
            global EMAIL_SUBJECT_TEXT 
            global EMAIL_BODY_TEXT 

            # PDFS_NAMES_LIST
            # Studnets Data
            # Subject & Body
            EMAIL_SUBJECT_TEXT = self.master.middleFrame.subjectTextBox.get("0.0", "end-1c")
            EMAIL_BODY_TEXT = self.master.middleFrame.bodyTextBox.get("0.0", "end-1c")
            
            if len(PDFS_LIST) == 0:
                messagebox.showerror(parent=self, title='Missing PDFs', message='Missing PDFs, make suer valid list of pdfs is loaded')
                return
            elif len(STUDENTS_LIST) == 0: 
                messagebox.showerror(parent=self, title='Missing Students Data', message='Missing Students Data, make suer valid list of students is loaded')
                return
            elif len(EMAIL_SUBJECT_TEXT) == 0:
                messagebox.showerror(parent=self, title='Missing Email Subject Text', message='Please Pate a Valid email subject in the subject area')
                return
            elif len(EMAIL_BODY_TEXT) == 0:
                messagebox.showerror(parent=self, title='Missing Email Body Text', message='Please Pate a Valid email body in the email body area')
                return
            
            formattedData = formatData(PDFS_LIST, STUDENTS_LIST, EMAIL_SUBJECT_TEXT, EMAIL_BODY_TEXT)
            studentsWithMissingPapers = []
            missingPaper = False

            for studnetId, data in formattedData.items():
                if len(data['papers']) == 0:
                    studentsWithMissingPapers.append(studnetId)
                    missingPaper = True

            if missingPaper:
                messagebox.showerror(parent=self, title="Studnets With Missing Papers", message=f"Students with Ids: {studentsWithMissingPapers} have missing papers, aborting...")
                return
            
            print("Calling the master navigateToEmailSenderUtility")
            self.master.navigateToEmailSenderUtility(formattedData)


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

        # Remove these later (critical)
        self.leftSideBar.loadPDFsDir()
        self.leftSideBar.loadStudentsData()

    def navigateToWelcomScreen(self):
        self.master.navigateToWelcomScreen(self)

    def navigateToEmailSenderUtility(self, formattedData):
        # On hold the ResultsUtility
        # Open the emails Utility
        # On Release (Success: ReportUtility)
        self.master.navigateToEmailSenderUtility(formattedData)
            

    
    