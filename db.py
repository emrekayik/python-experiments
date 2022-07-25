from tkinter import *
import sqlite3 as sq
import datetime

window = Tk()
window.title("EK KÜTÜPHANE") 
window.geometry('800x600+50+50')
header = Label(window, text="EK KÜTÜPHANE", font=("arial",30,"bold"), fg="steelblue").pack()

con = sq.connect('sistem.db')
c = con.cursor()

L1 = Label(window, text="Öğrencinin Adı", font=("arial",18)).place(x=10,y=100)
L2 = Label(window,text="Öğrencinin Sınıfı", font=("arial",18)).place(x=10,y=150)
L3 = Label(window,text="Kitabın Adı", font=("arial",18)).place(x=10,y=200)
L4 = Label(window,text="Kitabın Alındığı Gün", font=("arial",18)).place(x=10,y=250)

comp = StringVar(window)
comp.set('----')

compdb = StringVar(window)
compdb.set('----')

name = StringVar(window)
clas = StringVar(window)
bname = StringVar(window)
day = StringVar(window)


nameT = Entry(window, textvariable=name)
nameT.place(x=250, y=110)

clasT = Entry(window, textvariable=clas)
clasT.place(x=250, y=160)

bnameT = Entry(window, textvariable=bname)
bnameT.place(x=250, y=210)

dayT = Entry(window, textvariable=day)
dayT.place(x=250, y=260)


def get():
    print("Bir kayıt gönderdiniz")
    c.execute('CREATE TABLE IF NOT EXISTS ' + comp.get()+ ' (Datestamp TEXT, MaxWeight INTEGER, Reps INTEGER)')
    date = datetime.date(day.get(), clas.get(), bname.get(), name.get())

    c.execute(' INSERT INTO ' + comp.get()+ ' (Datestamp, MaxWeight, Reps) VALUES (?, ?, ?)',(name, clas, bname,name,day))

    con.commit()


    comp.set('----')
    name.set('')
    clas('')
    bname('')
    day('')


def clear():
    comp.set('----')
    name.set('')
    clas('')
    bname('')
    day('')


def record():
    c.execute('SELECT * FROM ' +compdb.get())
    frame = Frame(window)
    frame.place(x=400, y=150)

    Lb = Listbox(frame, height=8, width=25, font=("arial", 12))
    Lb.pack(side=LEFT, fill=Y)

    scroll = Scrollbar(frame, orient=VERTICAL)  # set scrollbar to list box for when entries exceed size of list box
    scroll.config(command=Lb.yview)
    scroll.pack(side=RIGHT, fill=Y)
    Lb.config(yscrollcommand=scroll.set)

    Lb.insert(0, 'Date, Max Weight, Reps')  # first row in listbox

    data = c.fetchall()  # Gets the data from the table

    for row in data:
        Lb.insert(1, row)  # Inserts record row by row in list box

    L7 = Label(window, text=compdb.get() + '',font=("arial", 16)).place(x=400, y=100)  # Title of list box, given which compound lift is chosen

    L8 = Label(window, text="They are ordered from most recent",font=("arial", 16)).place(x=400, y=350)
    con.commit()

    button_1 = Button(window, text="Ekle", command=get)
    button_1.place(x=300, y=300)

    button_2 = Button(window, text="Sil", command=clear)
    button_2.place(x=10, y=400)

    button_3 = Button(window, text="Veri Tabanını Aç", command=record)
    button_3.place(x=10, y=500)

    window.mainloop()
