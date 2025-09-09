from django.db import models
from django.utils import timezone
from django.urls import reverse


TITLE_CHOICES = (
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
)


# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.city} ({self.code})"



class Flight(models.Model):
    flight_no = models.CharField(max_length=10)
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departures')
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrivals')
    departure_date = models.DateTimeField(default=timezone.now)
    arriving_date = models.DateTimeField(default=timezone.now)
    flight_duration = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.flight_no} {self.origin} to {self.destination}"

    def get_absolute_url(self):
        return reverse("flights2:flight_detail", kwargs={"id": self.id})



class Passenger(models.Model):
    title = models.CharField(max_length=3, choices=TITLE_CHOICES)
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")

    def __str__(self):
        return f"{self.first} {self.last}"

    def get_absolute_url(self):
        return reverse("flights2:passenger_detail", kwargs={"id": self.id})
