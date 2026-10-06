from django.forms import ModelForm
from .models import *

class FlightForm(ModelForm):
    class Meta:
        model=Flight
        fields='__all__'


class PassengerForm(ModelForm):
    class Meta:
        model=Passenger
        fields='__all__'


class BookingForm(ModelForm):
    class Meta:
        model=Booking
        fields='__all__'