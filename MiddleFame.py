import customtkinter
from CTkXYFrame import *


PDFS_LIST = list(); 
PDFS_NAMES_LIST = list()
EMAIL_SUBJECT_TEXT = "MOCK TEST RESUTLS, YOUR CHILD'S SCRIPTS"
EMAIL_BODY_TEXT = '''
Please find attached your child’s scripts from the recent mock test taken on (Date).

Refer to the script in conjunction with the detailed feedback report you may already have received. If you are not yet in possession of the feedback report, please allow 3 days, as it is likely that your child’s paper is still being marked. As soon as the marking has been completed the feedback report will be emailed to you from 11plusfeedback.com.

Please check your spam folder if not received. Thank you.

Kind regards

Mock Test Masters.com


'''

class MiddleFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_rowconfigure(0, weight=100)
        self.grid_rowconfigure((1,2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.emailSubjectContent = customtkinter.CTkTextbox(self) 
        self.emailSubjectContent.insert("0.0", EMAIL_SUBJECT_TEXT)

        self.emailContentFrame = customtkinter.CTkTextbox(self) 
        self.emailContentFrame.insert("0.0", EMAIL_BODY_TEXT)
        self.tabularView = customtkinter.CTkScrollableFrame(self) # CTkXYFrame(self)

        self.emailSubjectContent.grid(row=0, column=0, padx="5", pady=5, sticky="nswe")
        self.emailContentFrame.grid(row=1, column=0, padx="5", pady="5", sticky="nswe")
        self.tabularView.grid(row=2, column=0, padx="5", pady="5", sticky="nswe")

