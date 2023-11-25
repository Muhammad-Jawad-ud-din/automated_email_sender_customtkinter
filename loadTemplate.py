import customtkinter
from tkinter import filedialog
from CTkTable import *
from CTkXYFrame import *

PDFS_LIST = list(); 
PDFS_NAMES_LIST = list()
SHEET_NAME = "AM"


def UploadAction(event=None):
    file = filedialog.askopenfile(filetypes=[("Text Files", ".docx .doc .txt")])
    print(file.name)
    with open(file.name, 'r') as stream:
        print(stream.getLine())

    # table = CTkTable(frame, row=len(arr), column=len(arr[0]), values=arr)
    # table.pack()

app = customtkinter.CTk()
app.geometry('500x300')
app.resizable(False, False)

button = customtkinter.CTkButton(app, text='Open', command=UploadAction)
button.pack(side="top", pady = 20)

frame = CTkXYFrame(app)
frame.pack(side='top', expand=True, fill="both")

app.mainloop()