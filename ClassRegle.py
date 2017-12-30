# -- coding: utf-8 --
class REGLE:
    def __init__(self,amorce,nomFichier,ext,aPartirDe,prefixe,postfixe,nomRegle=" ",nomDuFichier=" "):
        self.amorce=amorce
        self.nomFichier=nomFichier
        self.extension=ext
        self.aPartirDe=aPartirDe
        self.prefixe=prefixe
        self.postfixe=postfixe
        self.nomRegle=nomRegle
        if nomFichier == True:
            self.nomDuFichier=nomDuFichier
        else:
            self.nomDuFichier=" "
    def __str__(self):
        print(str(self.nomRegle)+","+str(self.amorce)+","+str(self.nomFichier)+","+str(self.extension)+","+str(self.aPartirDe)+","+str(self.prefixe)+","+str(self.postfixe)+","+str(self.nomDuFichier)+";")
    def GetNomRegle(self):
        return self.nomRegle
    def Get_amorce(self):
        return self.amorce
    def Set_amorce(self, amorce):
        self.amorce=amorce
    def Get_nomfichier(self):
        return self.nomfichier
    def Set_amorce(self, nomfichier):
        self.nomfichier=nomfichier
    def Get_nomDuFichier(self):
        return self.nomDuFichier
    def Set_nomDuFichier(self, nomDuFichier):
        if Get_nomfichier()== True:
            self.nomDuFichier=nomDuFichier
    def Get_aPartirDe(self):
        return self.aPartirDe
    def Set_aPartirDe(self, aPartirDe):
        self.aPartirDe=aPartirDe
    def Get_prefixe(self):
        return self.prefixe
    def Set_prefixe(self, prefixe):
        self.prefixe=prefixe
    def Get_postfixe(self):
        return self.postfixe
    def Set_postfixe(self, postfixe):
        self.postfixe=postfixe
    def Get_extension(self):
        extension=""
        for e in self.extension:
            extension=extension+e+", "
        return extension
    def Set_extension(self, extension):
        self.extension.append(extension)
