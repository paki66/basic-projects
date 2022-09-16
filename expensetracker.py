from inspect import stack
from operator import index
from re import T
import tkinter as tk
from tkinter import *
from tkinter.font import Font
import os


root = tk.Tk()

canvas = tk.Canvas(root, height=700, width=700, bg="green")
canvas.pack()

frame = tk.Frame(root, bg="gray")
frame.place(relwidth=0.9, relheight=0.7, relx=0.05, rely=0.25)


#stvaranje dviju traka za unos
traka_ime = tk.Entry(root, bg="white")
traka_ime.place(x=275, y=125)
traka_ime.insert(0, "ime transakcije:")

traka_iznosa = tk.Entry(root, bg="white")
traka_iznosa.place(x=275, y=150)
traka_iznosa.insert(0, 0)

#globalne varijable za zbrajanje ukupnog iznosa
ukupno_novaca = 0
iznosi = []
iznosi.append(0)
ukupan_iznos = tk.Label(frame, text="0")
rijec_ukupno = tk.Label(frame, text="Ukupan iznos na racunu je")

# kreiranje listboxa
transakcija = Listbox(frame, width=40, height=20, bg="white", selectbackground="#a6a6a6")
transakcija.pack()

 # funkcija za osvjezavanje ukupnog iznosa   
def obrisi_ukupno(widget):
    ukupan_iznos.destroy()
    rijec_ukupno.destroy()


def ispis(ukupno):
    global ukupan_ispis
    ukupan_ispis = IntVar()
    ukupan_ispis.set(ukupno)
    global ukupan_iznos
    ukupan_iznos = tk.Label(frame, textvariable=str(ukupan_ispis))
    ukupan_iznos.pack(side = BOTTOM)
    
    # ispis rijeci ukupno
    global rijec_ukupno
    rijec_ukupno = tk.Label(frame, text="Ukupan iznos na racunu je")
    rijec_ukupno.pack(side = BOTTOM)
    
    if ukupno_novaca < 0:
        rijec_ukupno.config(fg="red")
        ukupan_iznos.config(fg="red")

# funkcija za dodavanje transakcija; prihod parametar prati unosimo li prihod ili trošak
def dodaj_transakciju (prihod):
    
    # deklariranje potrebnih varijabla u funkciji
    global ukupno_novaca
    global iznosi
    global int_iznos
    int_iznos = int(traka_iznosa.get())
    prikaz_transakcije = traka_ime.get() + "   " + traka_iznosa.get() + " €"
    
    #selekcija u kojoj unosimo labelu za trosak ili prihod i zbrajamo ga u globalnu varijablu
    if prihod:
        transakcija.insert(END, prikaz_transakcije)
        transakcija.itemconfig(END, fg="green")
        iznosi.append(int_iznos)
    else:
        transakcija.insert(END, prikaz_transakcije)
        transakcija.itemconfig(END, fg="red")
        int_iznos = -abs(int_iznos)
        iznosi.append(int_iznos)        
        
    ukupno_novaca = ukupno_novaca + int_iznos
    ispis(ukupno_novaca)
    print(int_iznos)
    
       


def izbrisi_transakciju ():
    global ukupno_novaca
    ukupno_novaca = 0
    transakcija.delete(END)
    iznosi.pop()
    for i in iznosi:
        ukupno_novaca += i
    ispis(ukupno_novaca)
    
    
       
gumb_tr = tk.Button(root, text="trošak", padx=50, pady=10, fg="red", bg="white", command=lambda: [obrisi_ukupno(ukupan_iznos), dodaj_transakciju(0)])
gumb_tr.place(x=70, y=70) 

gumb_pr = tk.Button(root, text="prihod", padx=50, pady=10, fg="green", bg="white", command=lambda: [obrisi_ukupno(ukupan_iznos), dodaj_transakciju(1)])
gumb_pr.place(x=480, y=70) 

# gumb za brisanje
gumb_del = tk.Button(root, text="izbrisi", padx=50, pady=10, fg="black", bg="white", command=lambda: [obrisi_ukupno(ukupan_iznos), izbrisi_transakciju()])
gumb_del.place(x=275, y=70)



root.mainloop()
