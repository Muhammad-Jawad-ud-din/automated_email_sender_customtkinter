import customtkinter

class EmailsUtility(customtkinter.CTkToplevel):
    def __init__(self, master, size, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master 
        self.geometry(f"{size[0]}x{size[1]}")
        self.master.wait_window(self)

        # Top CTKScrollableFrame
        # Middle ProgressBar
        # Bottom Abort Button



