import customtkinter
from CTkXYFrame import * 

class FilesFrame(customtkinter.CTkScrollableFrame): # CTkXYFrame
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)