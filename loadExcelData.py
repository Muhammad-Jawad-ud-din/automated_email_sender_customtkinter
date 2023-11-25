import customtkinter
import os, numpy
from tkinter import filedialog
from CTkTable import *
from CTkXYFrame import *
import pandas as pd 

PDFS_LIST = list(); 
PDFS_NAMES_LIST = list()
SHEET_NAME = "AM"


def UploadAction(event=None):
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

    table = CTkTable(frame, row=len(arr), column=len(arr[0]), values=arr)
    table.pack()

app = customtkinter.CTk()
app.geometry('500x300')
app.resizable(False, False)

button = customtkinter.CTkButton(app, text='Open', command=UploadAction)
button.pack(side="top", pady = 20)

frame = CTkXYFrame(app)
frame.pack(side='top', expand=True, fill="both")

app.mainloop()