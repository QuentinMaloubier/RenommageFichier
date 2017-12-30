# -- coding: utf-8 --
from ClassRegle import *

class LISTEREGLE:
    def __init__(self, regles=[]):
        self.regles=regles
    def Get_regles(self):
        regle=""
        for r in self.regles:
            regle=regle+r.__str__()+"\n"
    def Set_regles(self, r):
        self.regles.append(r)
    def Charger(self):
        with open('renommage.ini','r') as file:
            file.read();
    def Sauvegarder(self):
        file.append(self.Get_regles())
