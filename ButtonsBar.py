import customtkinter
import numpy, os
from tkinter import filedialog
from CTkTable import *
from CTkXYFrame import *
import pandas as pd 

SHEET_NAME = "AM"
PDFS_LIST = list(); 
PDFS_NAMES_LIST = list()

class ButtonsBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)
        self.grid_rowconfigure(4, weight=40)

        self.grid_columnconfigure(0, weight=1)
        
        # add widgets onto the frame
        self.loadExcelBtn = customtkinter.CTkButton(self, text="Load Excel File", command=self.uploadExcelFile)
        self.loadDirBtn = customtkinter.CTkButton(self, text="Load Papers Folder", command=self.openPDFsDirectory)
        # self.loadTemplateBtn = customtkinter.CTkButton(self, text="Load Email Tempate")
        self.startBtn = customtkinter.CTkButton(self, text="Send Emails")
        self.clearBtn = customtkinter.CTkButton(self, text="Clear Lists", fg_color="gray", hover_color="red")
        
        self.loadExcelBtn.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="n")
        self.loadDirBtn.grid(row=1, column=0, padx=20, pady=(20, 0), sticky="n")
        # self.loadTemplateBtn.grid(row=2, column=0, padx=20, pady=(20, 0), sticky="n")
        self.startBtn.grid(row=3, column=0, padx=20, pady=(20, 0), sticky="n")
        self.clearBtn.grid(row=4, column=0, padx=20, pady=(20, 0), sticky="n")
    
    
    def uploadExcelFile(self, event=None):
        file = filedialog.askopenfile(filetypes=[("Excel files", ".xlsx .xls")])
        print(file.name)
        pdFile = pd.read_excel(file.name, SHEET_NAME)
        print(pdFile.head())
        columns = pdFile.columns.values.tolist()
        print(columns)
        arr = pdFile.to_numpy()
        print(arr)
        arr = numpy.insert(arr, 0, columns, axis=0).tolist()
        print(len(arr))
        print(len(arr[0]))
        print(type(arr))

        table = CTkTable(master=self.tabularView, row=len(arr), column=len(arr[0]), values=arr)
        table.pack()

    def openPDFsDirectory(self, event=None):
        directorypath = filedialog.askdirectory()

        print('Selected:', directorypath)
        for root, dirs, files in os.walk(directorypath):
            for file in files: 
                if file.endswith('.pdf'):
                    PDFS_LIST.append((file, os.path.join(os.path.abspath(root), file)))

        PDFS_NAMES_LIST = [[file[0]] for file in PDFS_LIST]
        print(PDFS_NAMES_LIST)
        table = CTkTable(self.filesFrame, row=len(PDFS_NAMES_LIST), column=1, values=PDFS_NAMES_LIST)
        table.pack()
