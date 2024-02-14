from django.db import models

class Airport(models.Model):
    name = models.CharField(max_length=255)
    airport_code = models.CharField(max_length=3)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Airline(models.Model):
    name = models.CharField(max_length=255)
    airline_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name

class Runway(models.Model):
    RUNWAY_DESIGNATION_CHOICES = [
        ('L', 'Left'),
        ('C', 'Center'),
        ('R', 'Right'),
        ('N', 'None')
    ]

    runway_number = models.IntegerField()
    runway_designation = models.CharField(max_length=1, choices=RUNWAY_DESIGNATION_CHOICES)
    length = models.IntegerField()
    width = models.IntegerField()
    airport = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='runways')

    def __str__(self):
        return f"{self.runway_number}{self.runway_designation}"

class Flight(models.Model):
    origin = models.ForeignKey('Airport', on_delete=models.PROTECT, related_name='flight_origin')
    destination = models.ForeignKey('Airport', on_delete=models.PROTECT, related_name='flight_destination')
    airline = models.ForeignKey('Airline', on_delete=models.PROTECT, related_name='flights')
    flight_number = models.IntegerField()
    departure = models.DateTimeField()
    arrival = models.DateTimeField()
    aircraft_type = models.CharField(max_length=10)

    def __str__(self):
        return f"Flight {self.flight_number}"
