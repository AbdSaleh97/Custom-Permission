from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from .models import Car
from .serializers import CarSerilaizer
from .permissions import CarOwner

# Create your views here.

class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerilaizer
    permission_classes = [IsAuthenticated]

class CarDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerilaizer
    permission_classes = [CarOwner]
