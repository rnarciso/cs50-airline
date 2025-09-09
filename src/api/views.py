from django.shortcuts import render
from rest_framework import viewsets
from flights.models import Airport, Flight, Passenger
from .serializers import AirportSerializer, FlightSerializer, PassengerSerializer

# Create your views here.
class AirportView(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer


class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerView(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer
