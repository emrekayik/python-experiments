from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
import datetime

# Defining TextEditor Class
class TextEditor:
    # Defining Constructor
    def __init__(self, root):
        # Assigning root
        self.root = root
        # Title of the window
        self.root.title("NotEK")
        # Window Geometry
        self.root.geometry("600x400+100+60")
        # Initializing filename
        self.filename = None
        # Declaring Title variable
        self.title = StringVar()
        # Declaring Status variable
        self.status = StringVar()
        # Creating Titlebar
        self.titlebar = Label(self.root, textvariable=self.title, font=("Monospace", 15, "bold"), bd=2, relief=GROOVE)
        # Packing Titlebar to root window
        self.titlebar.pack(side=TOP, fill=BOTH)
        # Calling Settitle Function
        self.settitle()
        # Creating Statusbar
        self.statusbar = Label(self.root, textvariable=self.status, font=("times new roman", 15, "bold"), bd=2, relief=GROOVE)
        # Packing status bar to root window
        self.statusbar.pack(side=BOTTOM, fill=BOTH)
        # Initializing Status
        self.status.set("NotEK")
        # Creating window logo
        root.wm_iconbitmap('EK.ico')
        # Creating Menubar
        self.menubar = Menu(self.root, font=("times new roman", 15, "bold"), activebackground="skyblue")
        # Configuring menubar on root window
        self.root.config(menu=self.menubar)
        # Creating File Menu
        self.filemenu = Menu(self.menubar, font=("times new roman", 12, "bold"), activebackground="skyblue", tearoff=0)
        # Adding New file Command
        self.filemenu.add_command(label="Yeni Dosya", accelerator="Ctrl+N", command=self.newfile)
        # Adding Open file Command
        self.filemenu.add_command(label="Dosya Aç", accelerator="Ctrl+O", command=self.openfile)
        # Adding Save File Command
        self.filemenu.add_command(label="Kaydet", accelerator="Ctrl+S", command=self.savefile)
        # Adding Save As file Command
        self.filemenu.add_command(label="Farklı Kaydet", accelerator="Ctrl+D", command=self.saveasfile)
        # Adding Seprator
        self.filemenu.add_separator()
        # Adding Exit window Command
        self.filemenu.add_command(label="Çıkış", accelerator="Ctrl+E", command=self.exit)
        # Cascading filemenu to menubar
        self.menubar.add_cascade(label="Dosya", menu=self.filemenu)
        # Creating Edit Menu
        self.editmenu = Menu(self.menubar, font=("times new roman", 12, "bold"), activebackground="skyblue", tearoff=0)
        # Adding Cut text Command
        self.editmenu.add_command(label="Kes", accelerator="Ctrl+X", command=self.cut)
        # Adding Copy text Command
        self.editmenu.add_command(label="Kopyala", accelerator="Ctrl+C", command=self.copy)
        # Adding Paste text command
        self.editmenu.add_command(label="Yapıştır", accelerator="Ctrl+V", command=self.paste)
        # Adding Select All text command
        self.editmenu.add_command(label="Tümünü Seç", accelerator="Ctrl+A", command=self.select_all)
        # Adding find text command
        self.editmenu.add_command(label="Bul", accelerator="Ctrl+F", command=self.find)
        # Adding Clock text command
        self.editmenu.add_command(label="Saat/Zaman", accelerator="Ctrl+T", command=self.time)
        # Adding Seprator
        self.editmenu.add_separator()
        # Cascading editmenu to menubar
        self.menubar.add_cascade(label="Düzenle", menu=self.editmenu)

        self.textmenu = Menu(self.menubar, font=("times new roman", 12, "bold"), activebackground="skyblue", tearoff=0)
        
        # Adding Text style cascade
        self.textmenu.add_command(label="Ortala", command=self.align_center)
        self.textmenu.add_command(label="Sola Yapıştır", command=self.align_left)
        self.textmenu.add_command(label="Sağa Yapıştır", command=self.align_right) 
        self.menubar.add_cascade(label="Yazı Tipi..", menu=self.textmenu)


        
        # Creating Help Menu
        self.helpmenu = Menu(self.menubar, font=("times new roman", 12, "bold"), activebackground="skyblue", tearoff=0)
        # Adding About Command
        self.helpmenu.add_command(label="Hakkında", command=self.infoabout)
        self.helpmenu.add_command(label="Yardım", command=self.infohelp)
        # Cascading helpmenu to menubar
        self.menubar.add_cascade(label="Yardım", menu=self.helpmenu)
        # Creating Scrollbar
        scrol_y = Scrollbar(self.root, orient=VERTICAL)
        # Creating Text Area
        self.txtarea = Text(self.root, yscrollcommand=scrol_y.set, font=("monospace", 15, "bold"), state="normal", relief=GROOVE)
        # Packing scrollbar to root window
        scrol_y.pack(side=RIGHT, fill=Y)
        # Adding Scrollbar to text area
        scrol_y.config(command=self.txtarea.yview)
        # Packing Text Area to root window
        self.txtarea.pack(fill=BOTH, expand=1)
        # Calling shortcuts funtion
        self.shortcuts()
    # Defining settitle function
    def settitle(self):
        # Checking if Filename is not None
        if self.filename:
            # Updating Title as filename
            self.title.set(self.filename)
        else:
            # Updating Title as Untitled
            self.title.set("Başlıksız")

    # Defining New file Function
    def newfile(self, *args):
        op = messagebox.askyesno("UYARI", "Kaydedilmemiş Dosyalarınız Kaybolabilir!!")
        if op > 0:
            self.txtarea.delete("1.0", END)
            # Updating filename as None
            self.filename = None
            # Calling settitle funtion
            self.settitle()
            # updating status
            self.status.set("Yeni Dosya Oluşturuldu")
        else:
            'return'



    # Defining Open File Funtion
    def openfile(self, *args):
        # Exception handling
        try:
            # Asking for file to open
            self.filename = filedialog.askopenfilename(title="Dosya Seç", filetypes=(("Tüm Dosyalar", "*.*"), ("Metin Dosyası", "*.txt"), ("Python Dosyası", "*.py"),("HTML Dosyası","*.html")))
            # checking if filename not none
            if self.filename:
                # opening file in readmode
                infile = open(self.filename, "r")
                # Clearing text area
                self.txtarea.delete("1.0", END)
                # Inserting data Line by line into text area
                for line in infile:
                    self.txtarea.insert(END, line)
                # Closing the file
                infile.close()
                # Calling Set title
                self.settitle()
                # Updating Status
                self.status.set("Başarıyla Açıldı")
        except Exception as e:
            messagebox.showerror("HATA", e)

    # Defining Save File Funtion
    def savefile(self, *args):
        # Exception handling
        try:
            # checking if filename not none
            if self.filename:
                # Reading the data from text area
                data = self.txtarea.get("1.0", END)
                # opening File in write mode
                outfile = open(self.filename, "w")
                # Writing Data into file
                outfile.write(data)
                # Closing File
                outfile.close()
                # Calling Set title
                self.settitle()
                # Updating Status
                self.status.set("Kaydetme Başarılı")
            else:
                self.saveasfile()
        except Exception as e:
            messagebox.showerror("HATA", e)

    # Defining Save As File Funtion
    def saveasfile(self, *args):
        # Exception handling
        try:
            # Asking for file name and type to save
            untitledfile = filedialog.asksaveasfilename(title="Dosyayı Farklı Kaydet", defaultextension=".txt", initialfile="Başlıksız.txt", filetypes=(("Tüm Dosyalar", "*.*"), ("Metin Dosyası", "*.txt"), ("Python Dosyası", "*.py"),("HTML Dosyası","*.html")))
            # Reading the data from text area
            data = self.txtarea.get("1.0", END)
            # opening File in write mode
            outfile = open(untitledfile, "w")
            # Writing Data into file
            outfile.write(data)
            # Closing File
            outfile.close()
            # Updating filename as Untitled
            self.filename = untitledfile
            # Calling Set title
            self.settitle()
            # Updating Status
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
                

    # Defining Time Function
    def time(self,*args):
        now = datetime.datetime.now()
        self.txtarea.insert(INSERT,now.strftime("%H:%M:%S %d-%m-%Y"))


    # Defining About Funtion
    def infohelp(self):
        messagebox.showinfo("YARDIM", "DOSYA SEÇENEKLERİ\nYeni Dosya : Bu seçeneği seçerek yeni metin dosyalarınızı oluşturabilirsiniz.\n\nDosya Aç : Bu seçeneği seçerek bilgisayarınızda bulunan dosyalardan birini seçebilirsiniz.\n\nKaydet : Bu seçeneği seçerek oluşturduğunuz dosyayı bilgisayarınıza kaydedebilirsiniz.\n\nFarklı Kaydet : Bu seçeneği seçerek Oluşturduğunuz dosyayı bilgisyarınıza farklı kaydedebilirsiniz.\n\n\nKISAYOL TUŞLARI\nCtrl+N  : Yeni Dosya\nCtrl+O  : Dosya Aç\nCtrl+S  : Kaydet\nCtrl+A  : Farklı Kaydet\nCtrl+E  : Çıkış\nCtrl+X  : Kes\nCtrl+C  : Kopyala\nCtrl+V  : Yapıştır\nCtrl+U  : Geri Al")


    def infoabout(self):
        messagebox.showinfo("NotEK", "NotEK basit metin editörü\nEmre KAYIK TARAFINDAN OLUŞTURULMUŞTUR.\nSÜRÜM :  2.0")


    def align_center(self):
        text_content = self.txtarea.get("1.0", 'end')
        self.txtarea.tag_config('center', justify=CENTER)
        self.txtarea.delete("1.0",END)
        self.txtarea.insert(INSERT,text_content,'center')
        self.status.set("METİN ORTALANDI")
            
    def align_left(self):
        text_content = self.txtarea.get(1.0, 'end')
        self.txtarea.tag_config('left', justify=LEFT)
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(INSERT,text_content,'left')
        self.status.set("METİN SOLA YAPIŞTIRILDI")

        
    def align_right(self):
        text_content = self.txtarea.get(1.0, 'end')
        self.txtarea.tag_config('right', justify=RIGHT)
        self.txtarea.delete(1.0,END)
        self.txtarea.insert(INSERT,text_content,'right')
        self.status.set("METİN SAĞA YAPIŞTIRILDI")


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
        # Binding Ctrl+t to time function
        self.txtarea.bind("<Control-t>", self.time)
        # Binding Ctrl+f to find function
        self.txtarea.bind("<Control-f>", self.find)
# Creating TK Container

root = Tk()
# Passing Root to TextEditor Class
TextEditor(root)
# Root Window Looping
root.mainloop()
