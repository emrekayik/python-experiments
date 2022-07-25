import sys
import os
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import datetime


class CodeEditor:
    def __init__(self, root):
        # Screen Options
        self.root = root
        self.root.title("NotEK")
        self.root.geometry("600x400+100+60")
        self.filename = None
        self.title = StringVar()
        self.status = StringVar()
        self.titlebar = Label(self.root, textvariable=self.title, font=("Monospace", 15, "bold"), bd=2, relief=GROOVE)
        self.titlebar.pack(side=TOP, fill=BOTH)
        self.settitle()
        self.statusbar = Label(self.root, textvariable=self.status, font=("times new roman", 15, "bold"), bd=2, relief=GROOVE)
        self.statusbar.pack(side=BOTTOM, fill=BOTH)
        self.status.set("NotEK")
        root.wm_iconbitmap('EK.ico')


        # Menu Options
        # File Menu Options
        self.menubar = Menu(self.root, font=("times new roman", 15, "bold"), activebackground="skyblue")
        self.root.config(menu=self.menubar)
        self.filemenu = Menu(self.menubar, font=("times new roman", 12, "bold"), activebackground="skyblue", tearoff=0)
        self.filemenu.add_command(label="Yeni Dosya", accelerator="Ctrl+N", command=self.newfile)
        self.filemenu.add_command(label="Dosya Aç", accelerator="Ctrl+O", command=self.openfile)
        self.filemenu.add_command(label="Kaydet", accelerator="Ctrl+S", command=self.savefile)
        self.filemenu.add_command(label="Farklı Kaydet", accelerator="Ctrl+D", command=self.saveasfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Çıkış", accelerator="Ctrl+E", command=self.exit)
        self.menubar.add_cascade(label="Dosya", menu=self.filemenu)


        # Edit Menu Options
        self.editmenu = Menu(self.menubar, font=("times new roman", 12, "bold"), activebackground="skyblue", tearoff=0)
        self.editmenu.add_command(label="Kes", accelerator="Ctrl+X", command=self.cut)
        self.editmenu.add_command(label="Kopyala", accelerator="Ctrl+C", command=self.copy)
        self.editmenu.add_command(label="Yapıştır", accelerator="Ctrl+V", command=self.paste)
        self.editmenu.add_command(label="Tümünü Seç", accelerator="Ctrl+A", command=self.select_all)
        self.editmenu.add_command(label="Bul", accelerator="Ctrl+F", command=self.find)
        self.editmenu.add_separator()
        self.menubar.add_cascade(label="Düzenle", menu=self.editmenu)


        # Code Panel Menu Options
        self.codemenu = Menu(self.menubar, font=("times new roman", 12, "bold"), activebackground="skyblue", tearoff=0)
        self.codemenu.add_command(label="HTML Örneği", accelerator="Ctrl+H", command=self.html_sample)
        self.menubar.add_cascade(label="Kod Menüsü", menu=self.codemenu)

        # Help Menu Options
        self.helpmenu = Menu(self.menubar, font=("times new roman", 12, "bold"), activebackground="skyblue", tearoff=0)
        self.helpmenu.add_command(label="Hakkında", command=self.infoabout)
        self.helpmenu.add_command(label="Yardım", command=self.infohelp)
        self.menubar.add_cascade(label="Yardım", menu=self.helpmenu)


        # Adding Screen Elements
        scrol_y = Scrollbar(self.root, orient=VERTICAL)
        self.txtarea = Text(self.root, yscrollcommand=scrol_y.set, font=("monospace", 15, "bold"), state="normal", relief=GROOVE)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        self.shortcuts()

    # Defining Functions
    # Defining settitle function
    def settitle(self):
        if self.filename:
            self.title.set(self.filename)
        else:
            self.title.set("Başlıksız")



    # Defining New file Function
    def newfile(self, *args):
        op = messagebox.askyesno("UYARI", "Kaydedilmemiş Dosyalarınız Kaybolabilir!!")
        if op > 0:
            self.txtarea.delete("1.0", END)
            self.filename = None
            self.settitle()
            self.status.set("Yeni Dosya Oluşturuldu")
        else:
            'return'



    # Defining Open File Funtion
    def openfile(self, *args):
        try:
            self.filename = filedialog.askopenfilename(title="Dosya Seç", filetypes=(("Tüm Dosyalar", "*.*"), ("Metin Dosyası", "*.txt"), ("Python Dosyası", "*.py"),("HTML Dosyası","*.html")))
            if self.filename:
                infile = open(self.filename, "r")
                self.txtarea.delete("1.0", END)
                for line in infile:
                    self.txtarea.insert(END, line)
                infile.close()
                self.settitle()
                self.status.set("Başarıyla Açıldı")
        except Exception as e:
            messagebox.showerror("HATA", e)



    # Defining Save File Funtion
    def savefile(self, *args):
        try:
            if self.filename:
                data = self.txtarea.get("1.0", END)
                outfile = open(self.filename, "w")
                outfile.write(data)
                outfile.close()
                self.settitle()
                self.status.set("Kaydetme Başarılı")
            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror("HATA", e)



    # Defining Save As File Funtion
    def saveasfile(self, *args):
        try:
            untitledfile = filedialog.asksaveasfilename(title="Dosyayı Farklı Kaydet", defaultextension=".txt", initialfile="Başlıksız.txt", filetypes=(("Tüm Dosyalar", "*.*"), ("Metin Dosyası", "*.txt"), ("Python Dosyası", "*.py"),("HTML Dosyası","*.html")))
            data = self.txtarea.get("1.0", END)
            outfile = open(untitledfile, "w")
            outfile.write(data)
            outfile.close()
            self.filename = untitledfile
            self.settitle()
            self.status.set("Kaydetme Başarılı")
        except Exception as e:
            messagebox.showerror("HATA", e)



    # Defining Exit Funtion
    def exit(self, *args):
        op = messagebox.askyesno("UYARI", "Kaydedilmemiş Dosyalarınız Kaybolabilir!!")
        if op > 0:
            self.root.destroy()
        else:
            'return'



    # Defining Cut Function
    def cut(self, *args):
        self.txtarea.event_generate("<<Cut>>")



    # Defining Copy Funtion
    def copy(self, *args):
        self.txtarea.event_generate("<<Copy>>")



    # Defining Paste Funtion
    def paste(self, *args):
        self.txtarea.event_generate("<<Paste>>")


    # Defining Select All Function
    def select_all(self,*args):
        self.txtarea.tag_add(SEL, "1.0",END)
        self.txtarea.mark_set(INSERT, "1.0")
        self.txtarea.see(INSERT)
    

    # Defining Find Function
    def find(self,*args):
        def handle(event):
            self.txtarea.tag_config('Bulundu',background='white',foreground='grey')
        self.txtarea.tag_remove("Bulundu",'1.0',END)
        find = simpledialog.askstring("BUL....","Kelimeyi gir :")
        if find:
            idx = '1.0'
        while 1:
                idx = self.txtarea.search(find,idx,nocase=1,stopindex=END)
                if not idx:
                    break
                lastidx = '%s+%dc' %(idx,len(find))
                self.txtarea.tag_add('Bulundu',idx,lastidx)
                idx = lastidx
                self.txtarea.tag_config('Bulundu',foreground='white',background='black')
                self.txtarea.bind("<1>",handle)

    # Defining HTML Sample Function
    def html_sample(self, *args):
        html = """<html>
    <head>
    </head>
    <body>
        <p>Hello World!</p>
    </body>
</html>"""
        self.txtarea.insert(INSERT,html)


    # Defining About Funtion
    def infohelp(self):
        messagebox.showinfo("YARDIM", "DOSYA SEÇENEKLERİ\nYeni Dosya : Bu seçeneği seçerek yeni metin dosyalarınızı oluşturabilirsiniz.\n\nDosya Aç : Bu seçeneği seçerek bilgisayarınızda bulunan dosyalardan birini seçebilirsiniz.\n\nKaydet : Bu seçeneği seçerek oluşturduğunuz dosyayı bilgisayarınıza kaydedebilirsiniz.\n\nFarklı Kaydet : Bu seçeneği seçerek Oluşturduğunuz dosyayı bilgisyarınıza farklı kaydedebilirsiniz.\n\n\nKISAYOL TUŞLARI\nCtrl+N  : Yeni Dosya\nCtrl+O  : Dosya Aç\nCtrl+S  : Kaydet\nCtrl+A  : Farklı Kaydet\nCtrl+E  : Çıkış\nCtrl+X  : Kes\nCtrl+C  : Kopyala\nCtrl+V  : Yapıştır\nCtrl+U  : Geri Al")


    def infoabout(self):
        messagebox.showinfo("NotEK", "NotEK basit metin editörü\nEmre KAYIK TARAFINDAN OLUŞTURULMUŞTUR.\nSÜRÜM :  2.0")
                
    def autocomplete(self):
        list_of_items = [open('html.txt')]

    # Defining shortcuts Funtion
    def shortcuts(self):
        # Binding Ctrl+n to newfile funtion
        self.txtarea.bind("<Control-n>", self.newfile)
        # Binding Ctrl+o to openfile funtion
        self.txtarea.bind("<Control-o>", self.openfile)
        # Binding Ctrl+s to savefile funtion
        self.txtarea.bind("<Control-s>", self.savefile)
        # Binding Ctrl+a to saveasfile funtion
        self.txtarea.bind("<Control-d>", self.saveasfile)
        # Binding Ctrl+e to exit funtion
        self.txtarea.bind("<Control-e>", self.exit)
        # Binding Ctrl+x to cut funtion
        self.txtarea.bind("<Control-x>", self.cut)
        # Binding Ctrl+c to copy funtion
        self.txtarea.bind("<Control-c>", self.copy)
        # Binding Ctrl+v to paste funtion
        self.txtarea.bind("<Control-v>", self.paste)
        # Binding Ctrl+a to select_all function
        self.txtarea.bind("<Control-a>", self.select_all())
        # Binding Ctrl+f to find function
        self.txtarea.bind("<Control-f>", self.find)
        # Binding Ctrl+h to html sample function
        self.txtarea.bind("<Control-h>", self.html_sample)
# Creating TK Container

root = Tk()
# Passing Root to TextEditor Class
CodeEditor(root)
# Root Window Looping
root.mainloop()
