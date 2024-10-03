import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        
        self.root = tk.Tk()
        
        self.menubar = tk.Menu(self.root)
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Close", command=self.on_closing)
        # self.filemenu.add_separator() # adds a sepeartor like -- in markdown
        self.filemenu.add_command(label="Close Without Question", command=exit)

        self.actionmenu = tk.Menu(self.menubar, tearoff=0)
        self.actionmenu.add_command(label="Show Message Box State", command=self.show_message)
        self.actionmenu.add_command(label="Show Message Box Checked", command=self.set_checked)
        self.actionmenu.add_command(label="Show Message Box Not Checked", command=self.set_unchecked)
        
        self.menubar.add_cascade(menu=self.filemenu, label="File")
        self.menubar.add_cascade(menu=self.actionmenu, label="Action")
        
        self.root.config(menu=self.menubar)
        
        self.label = tk.Label(self.root, text="Your Message", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)
        
        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text="Show Message", font=("Arial", 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        
        self.clearbtn = tk.Button(self.root, text="Clear", font=('Arial', 18), command=self.clear)
        self.clearbtn.pack(padx=10, pady=10)
        
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def show_message(self):
        # print(self.check_state.get()) # will print 0 if unchecked, 1 if checked
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END).rstrip()) # '1.0', tk.END means get everything in the box and return it, .rstrip removes any trailing characters and in this case it was newline
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))    
            
    def shortcut(self, event):
        if event.state == 4 and event.keysym == "Return":
            self.check_state.set(1)
            self.show_message()
            self.check_state.set(0)
            
    def on_closing(self):
        if messagebox.askyesno(title="Quit?", message = "Do you really want to quit?"):
            self.root.destroy()
            
    def clear(self):
        self.textbox.delete('1.0', tk.END)

    def set_checked(self):
        self.check_state.set(1)
        self.show_message()

    def set_unchecked(self):
        self.check_state.set(0)
        self.show_message()
        
MyGUI()