from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.contrib import messages
from .models import Airport, Flight, Passenger
from django.urls import reverse
from .forms import AirportModelForm, FlightModelForm, PassengerModelForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
    return render(request, 'flights3/index.html')


# ------------------------------ airport ------------------------------ #

class AirportListView(ListView):
    # template_name = 'flights3/airport_list.html'     # Override template page
    queryset = Airport.objects.all()



class AirportDetailView(DetailView):
    # template_name = 'flights3/airport_detail.html'   # Override template page
    queryset = Airport.objects.all()

    # def get_object(self):
    #     pk_ = self.kwargs.get('pk')
    #     return get_object_or_404(Airport, pk=pk_)



class AirportCreateView(CreateView):
    template_name = 'flights3/airport_create.html'
    form_class = AirportModelForm
    # queryset = Airport.objects.all()
    # success_url = '../'                                # Override success url

    # def form_valid(self, form):
    #     # print(form.cleaned_data)
    #     return super().form_valid(form)

    # def get_success_url(self):                         # method to override success url
    #     return '../'

    # def get_template_names(self):
    #     return 'flights3/airport_create.html'       # Override template page



class AirportUpdateView(UpdateView):
    template_name = 'flights3/airport_update.html'    # Override default template page <app_name>/<model_name>_form.html
    form_class = AirportModelForm

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Airport, pk=pk_)



class AirportDeleteView(DeleteView):
    template_name = 'flights3/airport_delete.html'   # Override default template page <app_name>/<model_name>_confirm_delete.html

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Airport, pk=pk_)

    def get_success_url(self):
        return '../../'




# ------------------------------ flight ------------------------------ #

class FlightListView(ListView):
    queryset = Flight.objects.all()



class FlightDetailView(DetailView):
    queryset = Flight.objects.all()

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Flight, pk=pk)
        passengers = obj.passengers.all()
        context = {
            "object": obj,
            "passengers": passengers
        }
        return context



class FlightCreateView(CreateView):
    template_name = 'flights3/flight_create.html'
    form_class = FlightModelForm



class FlightUpdateView(UpdateView):
    template_name = 'flights3/flight_update.html'
    form_class = FlightModelForm

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Flight, pk=pk_)



class FlightDeleteView(DeleteView):
    template_name = 'flights3/flight_delete.html'

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Flight, pk=pk_)

    def get_success_url(self):
        return '../../'





# ------------------------------ passenger ------------------------------ #

class PassengerListView(ListView):
    queryset = Passenger.objects.all()



class PassengerDetailView(DetailView):
    queryset = Passenger.objects.all()

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get('pk')
        obj = get_object_or_404(Passenger, pk=pk)
        flights = obj.flights.all()
        non_flights = Flight.objects.exclude(passengers=obj)
        context = {
            "object": obj,
            "flights": flights,
            "non_flights": non_flights
        }
        return context



class PassengerCreateView(CreateView):
    template_name = 'flights3/passenger_create.html'
    form_class = PassengerModelForm



class PassengerUpdateView(UpdateView):
    template_name = 'flights3/passenger_update.html'
    form_class = PassengerModelForm

    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Passenger, pk=pk_)



class PassengerDeleteView(DeleteView):
    template_name = 'flights3/passenger_delete.html'
    
    def get_object(self):
        pk_ = self.kwargs.get('pk')
        return get_object_or_404(Passenger, pk=pk_)

    def get_success_url(self):
        return '../../'



























# ------------------------------ airport ------------------------------ #

def airport_list_view(request):
    queryset = Airport.objects.all()

    context = {
        "object_list": queryset
    }
    return render(request, 'flights3/airport_list.html', context)



def airport_detail_view(request, pk):
    obj = get_object_or_404(Airport, pk=pk)

    context = {
        "object": obj
    }
    return render(request, 'flights3/airport_detail.html', context)



# def airport_create_view(request):
#     if request.method == 'POST':
#         Airport.objects.create(
#             code = request.POST["code"],
#             city = request.POST["city"]
#             )
#         return HttpResponseRedirect(reverse("flights3:airport_list"))
#     else:
#         airport_form = AirportForm()

#         context = {
#             "airport_form": airport_form
#             }
#         return render(request, 'flights3/airport_create.html', context)



# def airport_create_view(request):
#     airport_form = AirportForm(request.POST or None)
#     if airport_form.is_valid():
#         Airport.objects.create(**airport_form.cleaned_data)
#         messages.success(request, 'Airpot added successfully')
#         return HttpResponseRedirect(reverse("flights3:airport_list"))

#     context = {
#         "airport_form": airport_form
#         }
#     return render(request, 'flights3/airport_create.html', context)



def airport_create_view(request):
    form = AirportModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("../")

    context = {
        "form": form
        }
    return render(request, 'flights3/airport_create.html', context)



def airport_update_view(request, pk):
    obj = get_object_or_404(Airport, pk=pk)
    form = AirportModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')

    context = {
        "form": form
    }
    return render(request, 'flights3/airport_update.html', context)



def airport_delete_view(request, pk):
    obj = get_object_or_404(Airport, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')

    context = {
        "object": obj
    }
    return render(request, 'flights3/airport_delete.html', context)







# ------------------------------ flight ------------------------------ #

def flight_list_view(request):
    queryset = Flight.objects.all()
    
    context = {
        "object_list": queryset
    }
    return render(request, 'flights3/flight_list.html', context)



def flight_detail_view(request, pk):
    obj = get_object_or_404(Flight, pk=pk)
    
    passengers = obj.passengers.all()

    context = {
        "object": obj,
        "passengers": passengers
    }
    return render(request, 'flights3/flight_detail.html', context)



def flight_create_view(request):
    form = FlightModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')

    context = {
        "form": form
    }
    return render(request, 'flights3/flight_create.html', context)



def flight_update_view(request, pk):
    obj = get_object_or_404(Flight, pk=pk)
    form = FlightModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')

    context = {
        "form": form
    }
    return render(request, 'flights3/flight_update.html', context)



def flight_delete_view(request, pk):
    obj = get_object_or_404(Flight, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')

    context = {
        "object": obj
    }
    return render(request, 'flights3/flight_delete.html', context)






# ------------------------------ passenger ------------------------------ #

def passenger_list_view(request):
    queryset = Passenger.objects.all()

    context = {
        "object_list": queryset
    }
    return render(request, 'flights3/passenger_list.html', context)



def passenger_detail_view(request, pk):
    obj = get_object_or_404(Passenger, pk=pk)

    flights = obj.flights.all()
    non_flights = Flight.objects.exclude(passengers=obj)

    context = {
        "object": obj,
        "flights": flights,
        "non_flights": non_flights
    }
    return render(request, 'flights3/passenger_detail.html', context)



def passenger_create_view(request):
    form = PassengerModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('../')

    context = {
        "form": form
    }
    return render(request, 'flights3/passenger_create.html', context)



def passenger_update_view(request, pk):
    obj = get_object_or_404(Passenger, pk=pk)
    form = PassengerModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('../')

    context = {
        "form": form
    }
    return render(request, 'flights3/passenger_update.html', context)



def passenger_delete_view(request, pk):
    obj = get_object_or_404(Passenger, pk=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')

    context = {
        "object": obj
    }
    return render(request, 'flights3/passenger_delete.html', context)



def book_flight(request, pk):
    try:
        flight_id = int(request.POST["flight"])
        flight = Flight.objects.get(pk=flight_id)
        passenger = Passenger.objects.get(pk=pk)
    except KeyError:
        return render(request, "flights3/error.html", {"message": "No Selection!"})
    except Flight.DoesNotExist:
        return render(request, "flights3/error.html", {"message": "No Flight!"})
    except Passenger.DoesNotExist:
        return render(request, "flights3/error.html", {"message": "No Passenger!"})

    passenger.flights.add(flight)
    return HttpResponseRedirect(reverse('flights3:passenger_detail', args=(pk,)))
