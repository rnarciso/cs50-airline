from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('airports', views.AirportView)
router.register('flights', views.FlightView)
router.register('passengers', views.PassengerView)