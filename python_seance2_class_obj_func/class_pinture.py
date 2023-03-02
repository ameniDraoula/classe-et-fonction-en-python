import os
import platform
os.system('cls') 
class pintur:
    couleur = "blanc"
    def __init__(self,coul)
        self.couleur=coul
    def changer_couleur(self , nvcoul):
        self.couleur= nvcoul 
        return nvcoul
nvobj = pintur("rouge")
print( nvobj.changer_couleur("vert"))