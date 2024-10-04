import customtkinter

class TestButtonThemes():
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("350x350")
        self.create_ui()
        self.mode = "Dark Mode"
        self.theme = "Blue Theme"

        self.root.title(self.mode + " and " + self.theme)
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
        self.root.title(self.mode + " and " + self.theme)
        self.create_ui()
        
    def light(self):
        customtkinter.set_appearance_mode("light")
        self.mode = "Light Mode"
        self.recreate_ui()
        
    def dark(self):
        customtkinter.set_appearance_mode("dark")
        self.mode = "Dark Mode"
        self.recreate_ui()

    def green(self):
        customtkinter.set_default_color_theme("green")
        self.theme = "Green Theme"
        self.recreate_ui()

    def blue(self):
        customtkinter.set_default_color_theme("blue")
        self.theme = "Blue Theme"
        self.recreate_ui()

    def dark_blue(self):
        customtkinter.set_default_color_theme("dark-blue")
        self.theme = "Dark Blue Theme"
        self.recreate_ui()

TestButtonThemes()