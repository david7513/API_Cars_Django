from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer): # On définit notre serializer avec les champs suivants : 'immatriculation', 'marque', 'modele' et 'etat'
    class Meta:
        model = Car
        fields = ['immatriculation', 'marque', 'modele', 'etat']