from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):

    form=UserCreationForm(request.POST or None)

    if form.is_valid():
        user=form.save()
        login(request,user)
        return redirect('dashboard')

    return render(request,'form.html',{'form':form})


@login_required
def dashboard(request):

    search=request.GET.get('search')

    flights=Flight.objects.all()

    if search:
        flights=flights.filter(source__icontains=search)

    context={
        'flights':flights,
        'flight_count':Flight.objects.count(),
        'passenger_count':Passenger.objects.count(),
        'booking_count':Booking.objects.count()
    }

    return render(request,'dashboard.html',context)


@login_required
def add_flight(request):

    form=FlightForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request,'form.html',{'form':form})


@login_required
def edit_flight(request,id):

    flight=get_object_or_404(Flight,id=id)

    form=FlightForm(request.POST or None,instance=flight)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request,'form.html',{'form':form})


@login_required
def delete_flight(request,id):

    Flight.objects.get(id=id).delete()

    return redirect('dashboard')


@login_required
def add_passenger(request):

    form=PassengerForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request,'form.html',{'form':form})


@login_required
def book(request):

    form=BookingForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request,'form.html',{'form':form})