from django.db import models

class Flight(models.Model):
    flight_no=models.CharField(max_length=20)
    source=models.CharField(max_length=50)
    destination=models.CharField(max_length=50)
    departure=models.DateField()
    seats=models.IntegerField()

    def __str__(self):
        return self.flight_no


class Passenger(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
    passenger=models.ForeignKey(Passenger,on_delete=models.CASCADE)

    class Meta:
        unique_together=('flight','passenger')
