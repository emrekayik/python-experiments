from tkinter import *
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText
from tkinter  import messagebox
from tkinter.ttk import *
import re

root = Tk()
root.title('Text Editor')

#scrollable text

textPad = ScrolledText(root, width=100, height=50)
filename = ''


#functions

def newFile():
    global filename
    if len(textPad.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno("SAVE","Do you want to save?"):
            saveFile()
        else:
            textPad.delete(0.0,END)
    root.title("TEXT EDITOR")

def saveFile():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if f!= None:
        data = textPad.get('1.0',END)
    try:
        f.write(data)
    except:
        messagebox.showerror(title="Oops!!",message="Unable to save file!")
     
def saveAs():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    t = textPad.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        messagebox.showerror(title="Oops!!",message="Unable to save file!")

def openFile():
    f = filedialog.askopenfile(parent=root,mode='r')
    t = f.read()
    textPad.delete(0.0,END)
    textPad.insert(0.0,t)
    
def about_command():
    label = messagebox.showinfo("About", "Just Another TextPad \n Copyright \n No rights left to reserve")

def handle_click(event):
    textPad.tag_config('Found',background='white',foreground='grey')
    

def find_pattern():
    textPad.tag_remove("Found",'1.0',END)
    find = simpledialog.askstring("Find....","Enter text:")
    if find:
        idx = '1.0'
    while 1:
        idx = textPad.search(find,idx,nocase=1,stopindex=END)
        if not idx:
            break
        lastidx = '%s+%dc' %(idx,len(find))
        textPad.tag_add('Found',idx,lastidx)
        idx = lastidx
    textPad.tag_config('Found',foreground='white',background='black')
    textPad.bind("<1>",handle_click)

    '''
    t = textPad.get('1.0',END)
    occurance = t.upper().count(find.upper())
        
    if occurance > 0:
        label = messagebox.showinfo("Find",find+" has multiple occurances "+str(occurance))
    else:
        label = messagebox.showinfo("Find","No results")
       '''
def printme():
    label = messagebox.showinfo("Text","Welcome to text editor")

def exit_command():
    if messagebox.askyesno("Exit","Are you sure you want to exit?"):
        root.destroy()
    

#creating menu

menuM = Menu(root)
root.configure(menu=menuM)

fileM = Menu(menuM)
menuM.add_cascade(label='File',menu=fileM)
fileM.add_command(label='New',command=newFile)
fileM.add_command(label='Open',command=openFile)
fileM.add_command(label='Save',command=saveFile)
fileM.add_command(label='Save As...',command=saveAs)
fileM.add_separator()
fileM.add_command(label='Exit',command=exit_command)

editM = Menu(menuM)
menuM.add_cascade(label='Edit',menu=editM)
editM.add_command(label='Undo')
editM.add_command(label='Redo')
editM.add_command(label='Cut')
editM.add_command(label='Copy')
editM.add_command(label='Paste')

viewM = Menu(menuM)
menuM.add_cascade(label='View',menu=viewM)
viewM.add_command(label='Text',command=printme)

aboutM = Menu(menuM)
menuM.add_cascade(label='About',menu=aboutM)
aboutM.add_command(label='About',command = about_command)

findM = Menu(menuM)
menuM.add_cascade(label='Find',menu=findM)
findM.add_command(label='Find',command = find_pattern)


#adding icons

frame1=Frame(root)
frame1.pack()
Image1 = PhotoImage(file='new_file.gif')
l1 = Label(frame1,text='New file')
b1 = Button(frame1,image= Image1,command=newFile)
b1.grid(row=0,column=0)
l1.grid(row=1,column=0)
Image2 = PhotoImage(file='open_file.gif')
b2 = Button(frame1,image=Image2,command=openFile)
l2 = Label(frame1,text='Open file')
b2.grid(row=0,column=1)
l2.grid(row=1,column=1)
Image5 = PhotoImage(file='save.gif')
b5 = Button(frame1,image=Image5,command=saveAs)
l5 = Label(frame1,text='Save')
b5.grid(row=0,column=2)
l5.grid(row=1,column=2)
Image6 = PhotoImage(file='about.gif')
b6 = Button(frame1,image=Image6,command=about_command)
l6 = Label(frame1,text='About')
b6.grid(row=0,column=3)
l6.grid(row=1,column=3)
Image7 = PhotoImage(file='find_text.gif')
b7 = Button(frame1,image=Image7,command=find_pattern)
l7 = Label(frame1,text='Find text')
b7.grid(row=0,column=4)
l7.grid(row=1,column=4)

textPad.pack()

root.mainloop()



