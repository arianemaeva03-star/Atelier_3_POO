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
   def enterVoiture(self, voiture):
       if Voiture in self.listeVoitures:
           print("Voiture existe deja")
           return
       if len(self.listeVoitures) >= self.capacite:
           print("il y'a plus d'espace dans le parc")
           return
       self.listeVoitures.append(Voiture)
       print("la Voiture peut entrer")










