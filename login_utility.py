import smtplib 
import customtkinter
from tkinter import messagebox
from threading import Thread

FONT_FAMILY        = "Cascadia Mono"
SMTP_SERVER = "smtp.gmail.com" 
SMTP_PORT = 587

class LoginUtility(customtkinter.CTkToplevel):
    def __init__(self, master, size, **kwargs):
        try:
            super().__init__(master, **kwargs)
            
            def disable_close_event():
                return
            
            self.master = master 
            self.geometry(f"{size[0]}x{size[1]}")
            self.resizable(False, False)
            self.protocol("WM_DELETE_WINDOW", disable_close_event)   # DISABLE THE CLOSE BUTTON
            master.eval(f'tk::PlaceWindow {str(self)} center')
            
            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(1, weight=10)
            self.grid_columnconfigure(0, weight=1)

            self.font = customtkinter.CTkFont(family=FONT_FAMILY, size=14)
            self.headerFont = customtkinter.CTkFont(family=FONT_FAMILY, size=20)

            self.headerFrame = customtkinter.CTkLabel(self, text="Please Provide Your Credentials", font=self.headerFont)
            self.logInFrame = customtkinter.CTkFrame(self)
            self.headerFrame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
            self.logInFrame.grid(row=1, column=0, padx=60, pady=(0,20), sticky="nsew")

            self.logInFrame.grid_rowconfigure((0, 1, 2, 3), weight=1)
            self.logInFrame.grid_columnconfigure(0, weight=1)


            self.email_address_field = customtkinter.CTkEntry(self.logInFrame, placeholder_text="Email Address", font=self.font)
            self.password_field = customtkinter.CTkEntry(self.logInFrame, placeholder_text="Password", show="*", font=self.font)
            self.login_button = customtkinter.CTkButton(self.logInFrame, text="Log In", font=self.font, command=self.login_button_handler)

            self.email_address_field.grid(row=0, column=0, padx=30, pady=(10,5), sticky="ew")
            self.password_field.grid(row=1, column=0, padx=30, pady=(0, 5), sticky="ew")
            self.login_button.grid(row=2, column=0, padx=80, sticky="ew")

            self.master.wait_window(self)
        except Exception as exception:
            messagebox.showerror(title="Uh-Oh! Error Occured", message=exception)
            self.destroy()

    def login_button_handler(self):
        try:
            login_thread = Thread(target=self.login_thread_target)
            login_thread.start()
        except Exception as exception: 
            messagebox.showerror(title="Uh-Oh! Error Occured", message=exception)
            self.destroy()
            
    def login_thread_target(self):
        try:
            self.login_button.configure(state="disabled")
            self.email_address_field.configure(state="disabled")
            self.password_field.configure(state="disabled")

            session_email_address = self.email_address_field.get()
            session_password = self.password_field.get()
            mailer = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            mailer.ehlo()
            mailer.starttls()  # Enable encryption for secure connection
            mailer.ehlo()

            mailer.login(session_email_address, session_password)
            
            self.master.session_email_address = session_email_address
            self.master.mailer = mailer
            self.master.session_started = True
            self.destroy()

        except Exception as exception:
            print(exception)
            messagebox.showerror(parent=self, title='LogIn Failed', message=f"{exception}")
            self.login_button.configure(state="normal")
            self.email_address_field.configure(state="normal")
            self.password_field.configure(state="normal")
