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
   def entrerVoiture(self, voiture):
       if Voiture in self.listeVoitures:
           print(f"la Voiture existe deja")
           return
       if len(self.listeVoitures) >= self.capacite:
           print(f"il y'a plus d'espace dans le parc")
           return
       self.listeVoitures.append(Voiture)
       print(f"la Voiture peut entrer")
   def sortirVoiture(self, voiture):
       if voiture not in self.listeVoitures:
           print("la Voiture n'existe pas")
           return
       self.listeVoitures.remove(voiture)
       print(f"la Voiture peut sortir")
       print (f"place libre: {self.calculer_le_nombre_de_places_disponible}")
   def calculer_le_nombre_de_places_disponible(self):
       return self.capacite - len(self.listeVoitures)













