import customtkinter

class MiddleFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tempateArea = customtkinter.CTkScrollableFrame(self)
        self.tabularView = customtkinter.CTkScrollableFrame(self)

        self.tempateArea.grid(row=0, column=0, padx="5", pady="5", sticky="nswe")
        self.tabularView.grid(row=1, column=0, padx="5", pady="5", sticky="nswe")


