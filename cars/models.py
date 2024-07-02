from django.db import models

class Car(models.Model): # On définit les attributs de notre objet Car
    immatriculation = models.CharField(max_length=100, primary_key=True)
    marque = models.CharField(max_length=100)
    modele = models.CharField(max_length=100)
    etat = models.CharField(max_length=100)

    def __str__(self):
        return self.immatriculation
