# project.py
import tkinter as tk

root = tk.Tk()

display1 = tk.StringVar()
entry1 = tk.Entry(root,
    relief=tk.FLAT,
    textvariable=display1,
    justify='right',
    bg='orange')
entry1.pack()
entry1["font"] = "arial 30 bold"
    
root.mainloop()
