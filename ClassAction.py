# -- coding: utf-8 --
import os
class ACTION:
    def __init__(self, nomDuRépertoire, règle):
        self.nomDuRépertoire=nomDuRépertoire
        self.règle=règle
    def Get_nomDuRépertoire(self):
        return self.nomDuRépertoire
    def Set_nomDuRépertoire(self, nom):
        self.nomDuRépertoire=nom
    def Get_règle(self):
        return self.règle
    def Set_règle(self, règle):
        self.règle=règle
    def simule(self,repertoire, extension, prefixe, postfixe):
        for e in os.listdir():
            if e.endswith(extension):
                print(str(prefixe)+e+str(postfixe)+str(extension))
