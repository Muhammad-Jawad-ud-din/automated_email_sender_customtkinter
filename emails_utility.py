import customtkinter
import time
from threading import Thread
from email.message import EmailMessage

from tkinter import messagebox
from ctk_scrollable_table import CTkScrollableTable
from ctk_scrollable_frame import CTkXYScrollableFrame

FONT_FAMILY        = "Cascadia Mono"
SMTP_SERVER = "smtp.gmail.com" 
SMTP_PORT = 587
class EmailsUtility(customtkinter.CTkToplevel):
    def __init__(self, master, size, mailer, session_email_address, data, **kwargs):
        super().__init__(master, **kwargs)

        def disable_close_event():
            return

        self.geometry(f"{size[0]}x{size[1]}")
        self.protocol("WM_DELETE_WINDOW", disable_close_event)   # DISABLE THE CLOSE BUTTON
        self.resizable(False, False)

        self.master = master 
        self.data = data 
        self.session_email_address = session_email_address
        # self.session_password = session_password
        self.mailer = mailer
        self.sent = False

        self.grid_rowconfigure(0, weight=4)
        self.grid_rowconfigure((1,2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.button_font = customtkinter.CTkFont(family=FONT_FAMILY, size=16)
        # Top CTKScrollableFrame
        self.tabular_view = CTkXYScrollableFrame(self)
        

        # Middle ProgressBar
        self.progress_bar = customtkinter.CTkProgressBar(self, mode="determinate")
        self.progress_bar.set(0)

        # Bottom Abort Button
        self.abort_process_btn = customtkinter.CTkButton(self, text="Close Window", hover_color="red", font=self.button_font, command=self.abort_process_handler)
        self.start_process_btn = customtkinter.CTkButton(self, text="Start Process", font=self.button_font, command=self.send_emails_to_students)

        self.tabular_view.grid(row=0, column=0, padx=50, pady=(20, 10), sticky="nsew")
        self.progress_bar.grid(row=1, column=0, padx=50, pady=10, sticky="ew")
        self.abort_process_btn.grid(row=2, column=0, padx=200, pady=(10, 20), sticky="nse")
        self.start_process_btn.grid(row=2, column=0, padx=50, pady=(10, 20), sticky="nse")

        self.load_data_in_table()
        self.master.wait_window(self)
    
    def load_data_in_table(self):
        self.sent = False
        data = self.data
        students = list()

        for student_id, student_details in data.items():
            student_list = [student_id, student_details['email_address'], student_details['first_name'], student_details['full_name']]
            for paper_name, paper_path in student_details['papers']:
                student_list.append(paper_name)

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
        if self.sent:
            status = messagebox.askyesno(parent=self, title="Abort the current progress", message="Would you like to abort the current process?")
        else: 
            status = messagebox.askyesno(parent=self, title="Close Sender", message="Would you like to close the current window?")
        
        if status:
            self.destroy()

    def send_emails_to_students(self):
        sender_thread = Thread(target=self.sender_thread_target)
        sender_thread.start()

    def sender_thread_target(self):
        self.abort_process_btn.configure(text="Abort Sending")
        self.start_process_btn.configure(state='disabled')
        data = self.data
        total_length = len(data)
        step = 0
        delete_index = 1

        for student_id, student_details in data.items():
            try:
                student_message = self.create_email_template_for_student(student_details)
                self.mailer.send_message(student_message)
                self.students_table.delete_row(delete_index)
            except Exception as e: 
                delete_index += 1
            
            self.progress_bar.set(step + 1/total_length)
            step = step + 1/total_length

        self.abort_process_btn.configure(text="Close Window")
        self.sent = True
        messagebox.showinfo(parent=self, title='Proceess Completed', message="Emails failed for remaining students on list (if any)")

    def create_email_template_for_student(self, student):
        student_message = EmailMessage()
        student_message['Subject'] = student['subject']
        student_message['To'] = student['email_address']
        student_message['From'] = self.session_email_address
        student_message.set_content(student['email_body'])
        # student_message.add_alternative(f"""\{student['email_body']}""", subtype='html')
        
        for paper_name, paper_path in student['papers']:
            with open(paper_path,  'rb') as paper_file:
                paper_content = paper_file.read()
                student_message.add_attachment(paper_content, maintype='application', subtype = 'octet-stream', filename=paper_name)

        return student_message