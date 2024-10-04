import customtkinter
import requests

class UserInterface:
    def __init__(self):
        # Set appearance and theme
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        # Intitialize the resolution so it can be changed later
        self.resolution = "500x350"

        # Create main window
        self.root = customtkinter.CTk()
        self.root.geometry(self.resolution)
        
        # Create frame inside the main window
        self.frame = customtkinter.CTkFrame(master=self.root) 
        self.frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Create label for the login system
        self.label = customtkinter.CTkLabel(master=self.frame, text="Login System", font=("Impact", 24))
        self.label.pack(padx=10, pady=12)

        # Create entry for username
        self.entry1 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Username")
        self.entry1.pack(pady=12, padx=10)

        # Create entry for password
        self.entry2 = customtkinter.CTkEntry(master=self.frame, placeholder_text="Password", show="*")
        self.entry2.pack(pady=12, padx=10)

        # Create login button
        self.button = customtkinter.CTkButton(master=self.frame, text="Login", command=self.LogInService)
        self.button.pack(pady=12, padx=10)

        # Create "Remember me" checkbox
        self.checkbox = customtkinter.CTkCheckBox(master=self.frame, text="Remember me")
        self.checkbox.pack(pady=12, padx=10)

        # Window properties
        self.root.attributes("-topmost", True)
        self.root.resizable(False, False)
        self.root.mainloop()
        
    def LogInService(self):
        print("Login service called")
        print(self.resolution)
        self.username = self.entry1.get().rstrip()
        print(self.username)
        self.password = self.entry2.get().rstrip()
        print(self.password)
        # if requests.get('').text != 
        
        # You have to rebuild the GUI for it to resize properly
        
    def password_shortcut(self, event):
        pass

# Initialize the interface
Interface = UserInterface()
