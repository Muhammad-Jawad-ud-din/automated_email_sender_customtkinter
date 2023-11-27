import customtkinter
# NOTE: Start with the Students Results Utility


class LeftSideBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, kwargs)

        self.grid_rowconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Load PDFs Folder 
        # Load Excel File
        # Select Sheet_name appears after the excel is loaded
        # Go to WelcomeScreen
        # Empty row to push the Buttons upwards



class MiddleFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure((1,2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Subject TextArea
        # Email Body TextArea
        # Excel Loaded Table



class RightSideBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        #List of files that are loaded to the frame

class BottomButtonsBar(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.grid_columnconfigure((1,2), weight=1)

        # Empty Column to push buttons to right 
        # ClearTables Button 
        # SendEmails Button

class ResultsUtility(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure((0, 2), weight=1)
        self.grid_columnconfigure(1, weight=1)

        #LeftSideBar
        #MiddleFrame 
        #RightSideBar