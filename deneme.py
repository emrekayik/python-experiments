import sqlite3 as lite
from sqlite3 import Error
import tkinter as tk
from glob import glob
 
 
class App:
 
    def __init__(self, root):
        self.root = root
        self.root.geometry("200x200")
        self.root['bg'] = "cyan"
        tk.Button(
            self.root, text="Create a database",
            command=lambda: self.new_window(Win1)).pack()
        tk.Button(
            self.root, text="Create a table",
            command=lambda: self.new_window(Win2)).pack()
 
    def new_window(self, _class):
        self.new = tk.Toplevel(self.root)
        _class(self.new)
 
 
class Win:
    fields = []
 
    def listbox(self):
        self.lab_lb = tk.Label(self.root, text="Database in the folder")
        self.lab_lb['bg'] = 'gold'
        self.lab_lb.pack()
        self.lb = tk.Listbox(self.root)
        self.lb.pack()
        for file in glob("*.db"):
            self.lb.insert(tk.END, file)
        self.lb.bind("<Double-Button>", lambda x: self.show_selection())
 
    def show_selection(self):
        print("This function here does not works")
 
 
class Win1(Win):
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x300")
        self.root.title("Create Database")
        self.widgets_db()
        self.listbox()
 
    def widgets_db(self):
        self.label = tk.Label(
            self.root, text="Create a db [insert the name]")
        self.label.pack()
        self.db = tk.StringVar()
        self.e = tk.Entry(self.root, textvariable=self.db)
        self.e.pack()
        self.b = tk.Button(
            self.root, text="Create DB", command=lambda: self.mk_db())
        self.b.pack()
 
    def mk_db(self):
        db = self.e.get()
        if db.endswith(".db"):
            pass
        else:
            db = db + ".db"
        try:
            conn = lite.connect(db)
            if db in self.lb.get(0, tk.END):
                pass
            else:
                self.lb.insert(tk.END, db)
            return conn
        except Error as e:
            print(e)
        finally:
            self.db.set("")
            conn.close()
 
 
class Win2(Win):
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x500")
        self.root.title("Create Tables")
        self.listbox()
        self.widgets_tb()
        self.widgets_fl()
 
    def widgets_tb(self):
        """Widgets to create tables"""
        self.frame1 = tk.Frame(self.root)
        self.frame1.pack()
        self.lbdbn = tk.Label(
            self.frame1, text="Choose a Database")
        self.lbdbn.pack(side="left")
        # entry + StringVar
        self.string_dbn = tk.StringVar()
        # to get the value in the entry => a = self.string_tbn.get()
        # or a = self.entry_tbn.get()
        # if we want to clear the text into the entry => self.string_tbn("")
        self.entry_dbn = tk.Entry(
            self.frame1, textvariable=self.string_dbn)
        self.entry_dbn.pack(side="left")
 
        # ========== insert table data ===================
        # name of table
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack()
        self.lbtbn = tk.Label(
            self.frame2, text="Insert Table name")
        self.lbtbn.pack(side="left")
        self.string_tbn = tk.StringVar()
        self.entry_tbn = tk.Entry(
            self.frame2, textvariable=self.string_tbn)
        self.entry_tbn.pack(side="left")
 
    def widgets_fl(self):
        """The widgets to insert fields"""
        self.frame3 = tk.Frame(self.root)
        self.frame3.pack()
        self.lfl = tk.Label(
            self.frame3, text="Insert the table fields")
        self.lfl.pack()
        self.lfl['bg'] = 'gold'
        self.text = tk.Text(self.frame3, height=9)
        self.text.pack()
        self.btb = tk.Button(
            self.root, text="Create The table", command=lambda: self.mk_tb())
        self.btb.pack()
 
    def show_selection(self):
        x = self.lb.curselection()[0]
        x = self.lb.get(x)
        self.string_dbn.set(x)
 
    def mk_tb(self):
        self.conn = lite.connect(self.string_dbn.get())
        self.cur = self.conn.cursor()
        self.cur.execute(
            """create table {}(
            {});""".format(
                self.string_tbn,
                self.text.get("1.0", 'end-1c')))
 
 
root = tk.Tk()
app = App(root)
root.mainloop()
