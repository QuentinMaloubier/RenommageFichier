# -- coding: utf-8 --
from ClassAction import *
class RENOMMAGE(ACTION):
    def __init__(self, nomDuRépertoire, règle):
        ACTION.__init__(self, nomDuRépertoire, règle)
    def Renommer(self):
        for e in os.listdir():
            if e.endswith(self.règle.Get_extension()):
                newName=self.règle.Get_prefixe()+e+self.règle.Get_postfixe()+self.règle.Get_extension()
                os.rename(e,newName)
