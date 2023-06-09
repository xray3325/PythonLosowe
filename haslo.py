from tkinter import *
from tkinter import ttk
import random

alfabet = ['0','1','2','3','4','5','6','7','8','9','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'w', 'y', 'z','!','@','#','$','%','*','&','?']

def GenerujHaslo():
    haslo = []
    ZnakiSp = ZnakiSpecjalne.get()
    Lic = Liczby.get()
    i = 0
    while i < dlugosc.get():
        if  ZnakiSp == 1 and Lic == 1:
            letter = random.randrange(0,41)
        elif ZnakiSp == 1 and Lic == 0:
            letter = random.randrange(10,41)
        elif ZnakiSp == 0 and Lic == 1:
            letter = random.randrange(0,33)
        elif ZnakiSp == 0 and Lic == 0:
            letter = random.randrange(10,33)
        if bool(random.getrandbits(1)) == True:
            haslo.append(alfabet[letter])
        else:
            haslo.append(alfabet[letter].capitalize())
        i += 1
    haslo = ''.join(haslo)
    wynik.set(haslo)

def Zapisz():
    WygHaslo = wynik.get()
    file = open('/home/xray/Desktop/programowanie/geek.txt', 'a')
    if WygHaslo != '':
        file.write(WygHaslo + '\n')
    else:file.close()

root = Tk()
frm = ttk.Frame(root, padding=15)
frm.grid()

ttk.Label(frm, text="Czy chcesz użyć znaków specjalnych?", width=34, font=('', 15)).grid(column=0, row=0)
ttk.Label(frm, text="Czy chcesz użyć liczb 0-9?", width=34, font=('', 15)).grid(column=0, row=1)
ttk.Label(frm, text="Podaj Dlugość hasla: ", width=34, font=('', 15)).grid(column=0, row=2)
ttk.Label(frm, text="Wygenerowane haslo: ", width=34, font=('', 15)).grid(column=0, row=3)

dlugosc = IntVar()
ZnakiSpecjalne = IntVar()
Liczby = IntVar()
wynik = StringVar()

Checkbutton(frm, variable=ZnakiSpecjalne, width=5, selectcolor='lightgrey').grid(column=1, row=0)
Checkbutton(frm, variable=Liczby, width=5, selectcolor='lightgrey').grid(column=1, row=1)
Button(frm, text="Wygeneruj haslo", heigh=3, width=15, command=GenerujHaslo).grid(column=1, row=3, ipadx=10, sticky=NW)
Button(frm, text="Zapisz", height=3, width=15, command=Zapisz).grid(column=1, row=4,ipadx=10, sticky=SW)
Entry(frm, width=4, textvariable=dlugosc).grid(column=1, row=2)
l = Label(frm, height = 2, width=25, bg='light cyan', fg='black', font=('helvetica bold', 14), textvariable=wynik, anchor=W).grid(column=0, row=4,pady=3,ipadx=3, sticky=W)

root.mainloop()

