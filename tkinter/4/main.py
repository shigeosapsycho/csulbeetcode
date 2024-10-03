import customtkinter

class TestButtonThemes():
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("350x350")
        self.create_ui()

        self.root.title("Test CustomTkinter Colors")
        self.root.resizable(False, False)
        self.root.attributes("-topmost", True)
        self.root.mainloop()
        
    def create_ui(self):
        self.frame = customtkinter.CTkFrame(master=self.root)
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)       
         
        self.light_button = customtkinter.CTkButton(master=self.frame, text="Change to Light Mode", command=self.light)
        self.light_button.pack(pady=12, padx=10)
        
        self.dark_button = customtkinter.CTkButton(master=self.frame, text="Change to Dark Mode", command=self.dark)
        self.dark_button.pack(pady=12, padx=10)

        self.green_theme = customtkinter.CTkButton(master=self.frame, text="Change theme to green", command=self.green)
        self.green_theme.pack(pady=12, padx=10)
        
        self.blue_theme = customtkinter.CTkButton(master=self.frame, text="Change theme to blue", command=self.blue)
        self.blue_theme.pack(pady=12, padx=10)
        
        self.dark_blue_theme = customtkinter.CTkButton(master=self.frame, text="Change theme to dark-blue", command=self.dark_blue)
        self.dark_blue_theme.pack(pady=12, padx=10)

    def recreate_ui(self):
        self.frame.destroy()
        self.create_ui()
        
    def light(self):
        customtkinter.set_appearance_mode("light")
        self.recreate_ui()
        
    def dark(self):
        customtkinter.set_appearance_mode("dark")
        self.recreate_ui()

    def green(self):
        customtkinter.set_default_color_theme("green")
        self.recreate_ui()

    def blue(self):
        customtkinter.set_default_color_theme("blue")
        self.recreate_ui()

    def dark_blue(self):
        customtkinter.set_default_color_theme("dark-blue")
        self.recreate_ui()

TestButtonThemes()