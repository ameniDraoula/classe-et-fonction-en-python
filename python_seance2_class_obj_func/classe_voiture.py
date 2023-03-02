
# vous avez besoin de declaer et faire les variable d'initialisation , les parametre et le constructeur
import os
import platform
os.system('cls')

class Voiture:# creation dun classe voiture
    model=""
    vitesse=100
    couleur="noire"
    def __init__(self, model_arg, vitesse_arg , couleur_arg):
      self.model = model_arg
      self.vitesse = vitesse_arg
      self.couleur=couleur_arg

    def accelerer(self):# creation d'une fonction
    #ajoute 10 miles par heure à la vitesse actuelle
        self.vitesse = self.vitesse + 10;
        megan_objet = Voiture("Mégane", 100, "noire") # creation d'un objet et passer les parametre
        renault = Voiture("renault", 200, "rouge")

     
     
renault = Voiture("Mégane", 200, "rouge")
marsades = Voiture("marsades", 70, "noire")
volsvagin = Voiture("volsvagin", 90, "vert")
kia = Voiture("kia", 210, "bleu")
renault.accelerer()
print(renault .model)
print(renault.vitesse)
print(renault.couleur)
print("La vitesse actuelle: " + str(renault.vitesse))
