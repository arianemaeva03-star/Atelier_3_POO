class Voiture:
   def __init__(self, matricule, marque, couleur):
       self.matricule = matricule
       self.marque = marque
       self.couleur = couleur
   def afficher_Information(self):
       print(f"Voiture:{self.matricule} {self.marque} {self.couleur}")
class Parc:
   def __init__(self, id, adresse, capacite):
       self.id = id
       self.adresse = adresse
       self.capacite = capacite
       self.listeVoitures=[]



