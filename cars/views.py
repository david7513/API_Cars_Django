from rest_framework import viewsets
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Car
from .serializers import CarSerializer
from django.shortcuts import get_object_or_404


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()   # Récupère tous les objets Car de la base de données
    serializer_class = CarSerializer  # Utilise le serializer CarSerializer pour la sérialisation

    def create(self, request, *args, **kwargs): # On définit la méthode permettant d'ajouter de nouvelles voitures
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs): # On définit la méthode permettant de lister les voitures
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, id=None, *args, **kwargs): # On définit la méthode permettant de récupérer les objets de la base de données
        queryset = self.get_queryset()
        student = queryset.get(id=id)
        serializer = self.get_serializer(student)
        return Response(serializer.data)

    def put(request, id): # On définit la méthode permettant de mettre à jour les informations d'une voiture
        car = get_object_or_404(Car, id=id)
        serializer = CarSerializer(car, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(request, id): # On définit la méthode permettant de supprimer des voitures
        car = get_object_or_404(Car, id=id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

