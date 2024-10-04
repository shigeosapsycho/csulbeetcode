import tkinter as tk

# from tkinter import * # not the best practice to do since it can import more than you need

# Create the main window
root = tk.Tk()

root.geometry("500x500")
root.title("My First GUI")

label = tk.Label(root, text="Hello World!", font=('Arial', 18)) # text = text, (font = 'fontname', # of how big you want it in pts)
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Arial', 16)) # height = number for height, (font = 'fontname', # of how big you want in pts)
textbox.pack(padx=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text="1", font=('Arial',18))
btn1.grid(row=0, column=0, sticky=tk.W+tk.E) # tk.W and tk.E means West and East

btn2 = tk.Button(buttonframe, text="2", font=('Arial',18))
btn2.grid(row=0, column=1, sticky=tk.W+tk.E)

btn3 = tk.Button(buttonframe, text="3", font=('Arial',18))
btn3.grid(row=0, column=2, sticky=tk.W+tk.E)

btn4 = tk.Button(buttonframe, text="4", font=('Arial',18))
btn4.grid(row=1, column=0, sticky=tk.W+tk.E)

btn5 = tk.Button(buttonframe, text="5", font=('Arial',18))
btn5.grid(row=1, column=1, sticky=tk.W+tk.E)

btn6 = tk.Button(buttonframe, text="6", font=('Arial',18))
btn6.grid(row=1, column=2, sticky=tk.W+tk.E) 

buttonframe.pack(fill='x')  

# anotherbutton = tk.Button(root, text="TEST")
# anotherbutton.place(x=200, y=200, height=100, width=100)

# button = tk.Button(root, text="Click me!", font=('Arial', 18))
# button.pack(padx=10, pady=10)

# myentry = tk.Entry(root) # only one line and can't scroll down or up
# myentry.pack()

root.mainloop()
