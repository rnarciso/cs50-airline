from django.urls import path
from . import views

app_name = 'flights3'

urlpatterns = [
    path('', views.index, name="index"),

    path('airports/', views.AirportListView.as_view(), name="airport_list"),
    path('airports/add/', views.AirportCreateView.as_view(), name="airport_create"),
    path('airports/<int:pk>/', views.AirportDetailView.as_view(), name="airport_detail"),
    path('airports/<int:pk>/update/', views.AirportUpdateView.as_view(), name="airport_update"),
    path('airports/<int:pk>/delete/', views.AirportDeleteView.as_view(), name="airport_delete"),


    path('flights/', views.FlightListView.as_view(), name="flight_list"),
    path('flights/add/', views.FlightCreateView.as_view(), name="flight_create"),
    path('flights/<int:pk>/', views.FlightDetailView.as_view(), name="flight_detail"),
    path('flights/<int:pk>/update/', views.FlightUpdateView.as_view(), name="flight_update"),
    path('flights/<int:pk>/delete/', views.FlightDeleteView.as_view(), name="flight_delete"),


    path('passengers/', views.PassengerListView.as_view(), name="passenger_list"),
    path('passengers/add/', views.PassengerCreateView.as_view(), name="passenger_create"),
    path('passengers/<int:pk>/', views.PassengerDetailView.as_view(), name="passenger_detail"),
    path('passengers/<int:pk>/update/', views.PassengerUpdateView.as_view(), name="passenger_update"),
    path('passengers/<int:pk>/delete/', views.PassengerDeleteView.as_view(), name="passenger_delete"),







    # path('airports/', views.airport_list_view, name="airport_list"),
    # path('airports/add/', views.airport_create_view, name="airport_create"),
    # path('airports/<int:pk>/', views.airport_detail_view, name="airport_detail"),
    # path('airports/<int:pk>/update/', views.airport_update_view, name="airport_update"),
    # path('airports/<int:pk>/delete/', views.airport_delete_view, name="airport_delete"),


    # path('flights/', views.flight_list_view, name="flight_list"),
    # path('flights/add/', views.flight_create_view, name="flight_create"),
    # path('flights/<int:pk>/', views.flight_detail_view, name="flight_detail"),
    # path('flights/<int:pk>/update/', views.flight_update_view, name="flight_update"),
    # path('flights/<int:pk>/delete/', views.flight_delete_view, name="flight_delete"),

    # path('passengers/', views.passenger_list_view, name="passenger_list"),
    # path('passengers/add/', views.passenger_create_view, name="passenger_create"),
    # path('passengers/<int:pk>/', views.passenger_detail_view, name="passenger_detail"),
    # path('passengers/<int:pk>/update/', views.passenger_update_view, name="passenger_update"),
    # path('passengers/<int:pk>/delete/', views.passenger_delete_view, name="passenger_delete"),
    path('passengers/<int:pk>/book/', views.book_flight, name="book_flight"),
]
