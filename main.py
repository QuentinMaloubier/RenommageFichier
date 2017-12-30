# -- coding: utf-8 --
from tkinter import *
from tkinter.ttk import *
from ClassAction import *
from ClassRenommage import *
from ClassRegle import *
from ClassListRègle import *

def APropos():
    window=Tk()
    window.title('A propos de')
    texte = "Quentin MALOUBIER \n M2I L3 G1 \n 2017-2018 \n ITESCIA"
    lbContenu= Label(window, text=texte, borderwidth=1).grid(row=1, column=4)
    window.mainloop()
def Lister():
    lb=Listbox(fenetre)
    lb.pack()
    lesRègles=LISTEREGLE.charger()
    for r in lesRègles:
        lb.insert(END, r)
        
def NewRègle():
    fenetre=Tk()
    fenetre.title("Création d'une règle")
    lbTitre= Label(fenetre, text="Créer une règle", borderwidth=1).grid(row=1, column=4)
    lbEspace1= Label(fenetre, text=" ", borderwidth=1).grid(row=2, column=1)
    lbRègle= Label(fenetre, text="nom de la règle", borderwidth=1).grid(row=3, column=2)
    rRègle=StringVar()
    tbRègle= Entry(fenetre, textvariable=rRep).grid(row=3, column=4)
    lbEspace2= Label(fenetre, text="    ", borderwidth=1).grid(row=4, column=7)

    lbAmorce= Label(fenetre, text="amorce", borderwidth=1).grid(row=5, column=1)
    rAmorce = StringVar()
    amorcePossible= ('aucun', 'lettre', 'chiffre')
    cbAmorce = Combobox(fenetre, textvariable = rAmorce, values = amorcePossible, state = 'readonly').grid(row=6, column=1)

    lbPrefixe= Label(fenetre, text="préfixe", borderwidth=1).grid(row=5, column=2)
    rPrefixe=StringVar()
    tbPrefixe= Entry(fenetre, textvariable=rPrefixe).grid(row=6, column=2)

    value=False
    nomOriginal = Radiobutton(fenetre, text="", variable=value, value=False).grid(row=6, column=3)
    nomModifier = Radiobutton(fenetre, text="", variable=value, value=True).grid(row=7, column=3)

    lbNomFichier= Label(fenetre, text="nom du fichier").grid(row=5, column=4)
    rNomFichier=StringVar()
    lbNomOriginal= Label(fenetre, text="nom original").grid(row=6, column=4)
    tbNomFichier= Entry(fenetre, textvariable=rNomFichier).grid(row=7, column=4)

    lbPostfixe= Label(fenetre, text="postfixe", borderwidth=1).grid(row=5, column=5)
    rPostfixe=StringVar()
    tbPostfixe= Entry(fenetre, textvariable=rPostfixe).grid(row=6, column=5)

    lbExtension= Label(fenetre, text="extension concernée", borderwidth=1).grid(row=5, column=6)
    rExtension=StringVar()
    tbExtension= Entry(fenetre, textvariable=rExtension).grid(row=6, column=6)

    lbApartirDe= Label(fenetre, text="A partir de", borderwidth=1).grid(row=8, column=1)
    rAPartir=StringVar()
    tbApartirDe= Entry(fenetre, textvariable=rAPartir).grid(row=9, column=1)

    lbEspace2= Label(fenetre, text=" ", borderwidth=1).grid(row=10, column=7)
    créer= Button(fenetre, text='Créer', command=lambda: CréerRegle(rAmorce,value,rExtension,rAPartir,rPrefixe,rPostfixe,rRègle,rNomFichier)).grid(row=8, column=5)

    fenetre.mainloop()
def CréerRegle(amorce,nomFichier,Ext,aPartirDe,prefixe,postfixe,nomRegle,nomDuFichier):
    r1=REGLE.__init__(amorce,nomFichier,Ext,aPartirDe,prefixe,postfixe,nomRegle,nomDuFichier)
    lr=LISTEREGLE(r1)
    lr.Sauvegarder()

fenetre=Tk()
fenetre.title('Renommage de fichiers')
menuBar = Menu(fenetre)
fenetre['menu'] = menuBar
sousMenuRègles = Menu(menuBar)
menuBar.add_cascade(label='Règles', menu=sousMenuRègles)
sousMenuRègles.add_command(label='Lister', command=Lister)
sousMenuRègles.add_command(label='Créer', command=NewRègle)
menuBar.add_command(label='?', command=APropos)


lbTitre= Label(fenetre, text="renommage en lots", borderwidth=1).grid(row=1, column=4)
lbEspace1= Label(fenetre, text=" ", borderwidth=1).grid(row=2, column=1)
lbRepertoire= Label(fenetre, text="nom du répertoire", borderwidth=1).grid(row=2, column=2)
rRep=StringVar()
tbRepertoire= Entry(fenetre, textvariable=rRep).grid(row=2, column=4)

lbAmorce= Label(fenetre, text="amorce", borderwidth=1).grid(row=5, column=1)
amorcePossible= ('aucun', 'lettre', 'chiffre')
rAmorce=StringVar()
cbAmorce = Combobox(fenetre, textvariable = rAmorce, values = amorcePossible, state = 'readonly').grid(row=6, column=1)

lbPrefixe= Label(fenetre, text="préfixe", borderwidth=1).grid(row=5, column=2)
rPrefixe=StringVar()
tbPrefixe= Entry(fenetre, textvariable=rPrefixe).grid(row=6, column=2)

value=False
nomOriginal = Radiobutton(fenetre, text="", variable=value, value=False).grid(row=6, column=3)
nomModifier = Radiobutton(fenetre, text="", variable=value, value=True).grid(row=7, column=3)

lbNomFichier= Label(fenetre, text="nom du fichier").grid(row=5, column=4)
rNomFichier=StringVar()
lbNomOriginal= Label(fenetre, text="nom original").grid(row=6, column=4)
tbNomFichier= Entry(fenetre, textvariable=rNomFichier).grid(row=7, column=4)

lbPostfixe= Label(fenetre, text="postfixe", borderwidth=1).grid(row=5, column=5)
rPostfixe=StringVar()
tbPostfixe= Entry(fenetre, textvariable=rPostfixe).grid(row=6, column=5)

lbExtension= Label(fenetre, text="extension concernée", borderwidth=1).grid(row=5, column=6)
rExtension=""
tbExtension= Entry(fenetre, textvariable=rExtension).grid(row=6, column=6)

lbApartirDe= Label(fenetre, text="A partir de", borderwidth=1).grid(row=8, column=1)
rAPartir=StringVar()
tbApartirDe= Entry(fenetre, textvariable=rAPartir).grid(row=9, column=1)

lbEspace2= Label(fenetre, text=" ", borderwidth=1).grid(row=10, column=7)
r1=REGLE(rAmorce,value,rExtension,rAPartir,rPrefixe,rPostfixe,nomDuFichier=rNomFichier)
action=ACTION(rRep,r1)
renommer= Button(fenetre, text='Renommer', command=lambda: action.simule(rRep, rExtension, rPrefixe,rPostfixe)).grid(row=8, column=5)

can = Canvas(fenetre)
can.grid(row=2, column=7)
img = PhotoImage(file='renommage.png')
can.create_image(100, 100, image=img)


fenetre.mainloop()
