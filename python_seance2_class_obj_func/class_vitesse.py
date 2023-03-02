import os
import platform
os.system('cls')
#generer la documentation
"""documentation"""
class vitesse:
    #proprieter
    vitess_param = 70
    vitess_initial=0
    vitess_intermidiare=50
    vitess_final=300
    #constructeur
    def __init__(self, vitesse_arg , v_ini, v_inter , v_f ):
        self.vitess_param =vitesse_arg
        self.initial=v_ini
        self.vitess_intermidiare = v_inter
        self.vitess_final=v_f

    def calculer_vitess_moyen(self):
       vitess_intermidiare = (self.vitess_final-self.vitess_initial)/2
       return vitess_intermidiare
objt_vitess = vitesse(370 , 0, 50 ,180 )
print("la vitesse moyenne ="+objt_vitess.calculer_vitess_moyen())
