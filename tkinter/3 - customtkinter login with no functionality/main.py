# need to pip install customtkinter for it to work

import customtkinter

"""
# This is how basic tkinter is structured
import tkinter

root = tkinter.Tk()

label = tkinter.Label(root, )
label.pack()
"""

customtkinter.set_appearance_mode("light") # light or dark
customtkinter.set_default_color_theme("green") # 3 themes you can choose from, blue, green, dark-blue

root = customtkinter.CTk()
root.geometry("500x350") # in pixels

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Impact", 24))
label.pack(padx=10, pady=12)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remeber me")
checkbox.pack(pady=12, padx=10)

root.attributes("-topmost", True)
root.resizable(False, False) # width and height and prevents the user from resizing the box
root.mainloop()