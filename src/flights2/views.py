from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from .models import Airport, Flight, Passenger
from django.urls import reverse
from .forms import AirportForm, FlightModelForm, PassengerModelForm


# Create your views here.
def index(request):
    return render(request, 'flights2/index.html')


# ------------------------------ airport ------------------------------ #

def airport_list_view(request):
    queryset = Airport.objects.all()

    context = {
        "object_list": queryset
    }
    return render(request, 'flights2/airport_list.html', context)


# def airport_create_view(request):
#     if request.method == 'POST':
#         Airport.objects.create(
#             code = request.POST["code"],
#             city = request.POST["city"]
#             )
#         return HttpResponseRedirect(reverse("flights2:airport_list"))
#     else:
#         airport_form = AirportForm()

#         context = {
#             "airport_form": airport_form
#             }
#         return render(request, 'flights2/airport_create.html', context)



def airport_create_view(request):
    airport_form = AirportForm(request.POST or None)
    if airport_form.is_valid():
        Airport.objects.create(**airport_form.cleaned_data)
        messages.success(request, 'Airpot added successfully')
        return HttpResponseRedirect(reverse("flights2:airport_list"))

    context = {
        "airport_form": airport_form
        }
    return render(request, 'flights2/airport_create.html', context)



# def airport_create_view(request):
#     airport_form = AirportModelForm(request.POST or None)
#     if airport_form.is_valid():
#         airport_form.save()
#         return redirect("../")

#     context = {
#         "airport_form": airport_form
#         }
#     return render(request, 'flights2/airport_create.html', context)









# ------------------------------ flight ------------------------------ #

def flight_list_view(request):
    queryset = Flight.objects.all()
    
    context = {
        "object_list": queryset
    }
    return render(request, 'flights2/flight_list.html', context)



def flight_detail_view(request, id):
    try:
        flight = Flight.objects.get(pk=id)
    except Flight.DoesNotExist:
        raise Http404("Flight does not exist")
    
    passengers = flight.passengers.all()

    context = {
        "flight": flight,
        "passengers": passengers
    }
    return render(request, 'flights2/flight_detail.html', context)



def flight_create_view(request):
    flight_form = FlightModelForm(request.POST or None)
    if flight_form.is_valid():
        flight_form.save()
        return redirect('../')

    context = {
        "flight_form": flight_form
    }
    return render(request, 'flights2/flight_create.html', context)








# ------------------------------ passenger ------------------------------ #

def passenger_list_view(request):
    queryset = Passenger.objects.all()

    context = {
        "object_list": queryset
    }
    return render(request, 'flights2/passenger_list.html', context)



def passenger_detail_view(request, id):
    try:
        passenger = Passenger.objects.get(pk=id)
    except Passenger.DoesNotExist:
        raise Http404("Passenger does not exist")

    flights = passenger.flights.all()
    non_flights = Flight.objects.exclude(passengers=passenger)

    context = {
        "passenger": passenger,
        "flights": flights,
        "non_flights": non_flights
    }
    return render(request, 'flights2/passenger_detail.html', context)



def passenger_create_view(request):
    passenger_form = PassengerModelForm(request.POST or None)
    if passenger_form.is_valid():
        passenger_form.save()
        return redirect('../')

    context = {
        "passenger_form": passenger_form
    }
    return render(request, 'flights2/passenger_create.html', context)



def passenger_update_view(request, id):
    passenger_details = get_object_or_404(Passenger, id=id)
    passenger_form = PassengerModelForm(request.POST or None, instance=passenger_details)
    if passenger_form.is_valid():
        passenger_form.save()
        return redirect('../')

    context = {
        "passenger_form": passenger_form
    }
    return render(request, 'flights2/passenger_update.html', context)



def passenger_delete_view(request, id):
    obj = get_object_or_404(Passenger, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')

    context = {
        "object": obj
    }
    return render(request, 'flights2/passenger_delete.html', context)



def book_flight(request, id):
    try:
        flight_id = int(request.POST["flight"])
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=id)
    except KeyError:
        return render(request, "flights2/error.html", {"message": "No Selection!"})
    except Flight.DoesNotExist:
        return render(request, "flights2/error.html", {"message": "No Flight!"})
    except Passenger.DoesNotExist:
        return render(request, "flights2/error.html", {"message": "No Passenger!"})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse('flights2:passenger_detail', args=(id,)))
