import customtkinter
import os
from tkinter import filedialog
from CTkTable import *
from CTkXYFrame import *

PDFS_LIST = list(); 
PDFS_NAMES_LIST = list()

def UploadAction(event=None):
    directorypath = filedialog.askdirectory()
    
    print('Selected:', directorypath)
    for root, dirs, files in os.walk(directorypath):
        for file in files: 
            if file.endswith('.pdf'):
                PDFS_LIST.append((file, os.path.join(os.path.abspath(root), file)))

    PDFS_NAMES_LIST = [[file[0]] for file in PDFS_LIST]
    print(PDFS_NAMES_LIST)
    table = CTkTable(frame, row=len(PDFS_NAMES_LIST), column=1, values=PDFS_NAMES_LIST)
    table.pack()

app = customtkinter.CTk()
app.geometry('500x600')
app.resizable(False, False)

button = customtkinter.CTkButton(app, text='Open', command=UploadAction)
button.pack(side="left", padx = 20)

frame = CTkXYFrame(app)
frame.pack(side='left', expand=True, fill="both")

app.mainloop()