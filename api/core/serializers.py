from rest_framework import serializers
from core.models import Airline, Airport, Runway, Flight


from rest_framework import serializers
from core.models import Runway

class RunwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Runway
        fields = ['airport', 'runway_number', 'length', 'width']
        read_only_fields = ['id']

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['origin', 'destination', 'airline', 'departure', 'arrival', 'flight_number', 'aircraft_type']
        read_only_fields = ['id']

