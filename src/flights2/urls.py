from django.urls import path
from . import views

app_name = 'flights2'

urlpatterns = [
    path('', views.index, name="index"),

    path('airports/', views.airport_list_view, name="airport_list"),
    path('airports/add/', views.airport_create_view, name="airport_create"),

    path('flights/', views.flight_list_view, name="flight_list"),
    path('flights/add/', views.flight_create_view, name="flight_create"),
    path('flights/<int:id>/', views.flight_detail_view, name="flight_detail"),

    path('passengers/', views.passenger_list_view, name="passenger_list"),
    path('passengers/add/', views.passenger_create_view, name="passenger_create"),
    path('passengers/<int:id>/', views.passenger_detail_view, name="passenger_detail"),
    path('passengers/<int:id>/update/', views.passenger_update_view, name="passenger_update"),
    path('passengers/<int:id>/delete/', views.passenger_delete_view, name="passenger_delete"),
    path('passengers/<int:id>/book/', views.book_flight, name="book_flight"),
]
