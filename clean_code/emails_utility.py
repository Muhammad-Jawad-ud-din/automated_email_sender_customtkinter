import customtkinter

from tkinter import messagebox
from CTkScrollableTable import CTkScrollableTable
from CTkXYScrollableFrame import CTkXYScrollableFrame

FONT_FAMILY        = "Cascadia Mono"

class EmailsUtility(customtkinter.CTkToplevel):
    def __init__(self, master, size, email_address, password, data, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master 
        self.geometry(f"{size[0]}x{size[1]}")
        self.data = data 
        self.email_address = email_address
        self.password = password

        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure((1,2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.button_font = customtkinter.CTkFont(family=FONT_FAMILY, size=16)
        # Top CTKScrollableFrame
        self.tabular_view = CTkXYScrollableFrame(self)
        

        # Middle ProgressBar
        self.progress_bar = customtkinter.CTkProgressBar(self, mode="determinate")

        # Bottom Abort Button
        self.abort_process_btn = customtkinter.CTkButton(self, text="Abort Process", hover_color="red", font=self.button_font, command=self.abort_process_handler)

        self.tabular_view.grid(row=0, column=0, padx=50, pady=(20, 10), sticky="nsew")
        self.progress_bar.grid(row=1, column=0, padx=50, pady=10, sticky="ew")
        self.abort_process_btn.grid(row=2, column=0, padx=50, pady=(10, 20), sticky="nse")

        self.load_data_in_table()
        self.master.wait_window(self)
    
    def load_data_in_table(self):
        data = self.data
        students = list()

        for student_id, student_details in data.items():
            student_list = [student_id, student_details['email'], student_details['first_name'], student_details['full_name']]
            for paper in student_details['papers']:
                student_list.append(paper)

            students.append(student_list)

        columns_length = max(len(student) for student in students)
        headers_list = ['Student ID', 'Email Address', 'First Name', 'Full Name']
        for attachment_no in range(columns_length - 4):
            headers_list.append(f'Attachment {attachment_no + 1}')
        
        students.insert(0, headers_list)

        # NOTE (Data is not showing in the table)
        self.students_table = CTkScrollableTable(self.tabular_view, row=len(students), column=columns_length, values=students)
        self.students_table.grid(row=0, column=0, sticky="nsew")


    def abort_process_handler(self):
        messagebox.askokcancel(title="Abort the current progress", message="Would you like to abort the current process?")
        self.destroy()




