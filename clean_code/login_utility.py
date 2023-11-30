import customtkinter
from tkinter import messagebox

FONT_FAMILY        = "Cascadia Mono"
SMTP_SERVER = "smtp.titan.email" 
SMTP_PORT = 587

class LoginUtility(customtkinter.CTkToplevel):
    def __init__(self, master, size, **kwargs):
        super().__init__(master, **kwargs)

        self.master = master 
        self.geometry(f"{size[0]}x{size[1]}")
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


        self.usernameField = customtkinter.CTkEntry(self.logInFrame, placeholder_text="Email Address", font=self.font)
        self.passwordField = customtkinter.CTkEntry(self.logInFrame, placeholder_text="Password", show="*", font=self.font)
        self.logInButton = customtkinter.CTkButton(self.logInFrame, text="Log In", font=self.font, command=self.logInButtonHandler)

        self.usernameField.grid(row=0, column=0, padx=30, pady=(10,5), sticky="ew")
        self.passwordField.grid(row=1, column=0, padx=30, pady=(0, 5), sticky="ew")
        self.logInButton.grid(row=2, column=0, padx=80, sticky="ew")

        self.master.wait_window(self)

    def logInButtonHandler(self):
        self.logInButton.configure(state="disabled")
        emailAddress = self.usernameField.get()
        password = self.passwordField.get()
        
        try:    
            import smtplib 
            server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
            server.ehlo()
            server.starttls()  # Enable encryption for secure connection
            server.ehlo()

            server.login(emailAddress, password)
            
            self.master.session_email_address = emailAddress
            self.master.email_server = server
            self.master.session_started = True
            self.destroy()
        except Exception as exception:
            messagebox.showerror(parent=self, title='LogIn Failed', message=f"{exception}")
            self.logInButton.configure(state="normal")
