import customtkinter
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

        self.button_font = customtkinter.CTkFont(family=FONT_FAMILY, size=14)
        # Top CTKScrollableFrame
        self.tabular_view = CTkXYScrollableFrame(self)
        
        # Middle ProgressBar
        self.progress_bar = customtkinter.CTkProgressBar(self)

        # Bottom Abort Button
        self.bottom_buttons_frame = customtkinter.CTkFrame(self)
        self.bottom_buttons_frame.grid_rowconfigure(0, weight=1)
        self.bottom_buttons_frame.grid_columnconfigure(0, weight=1)
        self.abort_process_btn = customtkinter.CTkButton(self, text="Abort Process", hover_color="red", font=self.button_font)
        self.abort_process_btn.grid(row=0, column=0, padx=(0, 40), pady=10, sticky="e")

        self.tabular_view.grid(row=0, column=0, padx=50, pady=(20, 10), sticky="nsew")
        self.progress_bar.grid(row=1, column=0, padx=50, pady=10, sticky="ew")
        self.abort_process_btn.grid(row=2, column=0, padx=50, pady=(10, 20), sticky="nse")
        self.master.wait_window(self)




