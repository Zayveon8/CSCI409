from rest_framework import serializers
from core.models import Airline, Airport, Runway, Flight


from rest_framework import serializers
from core.models import Runway

class RunwaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Runway
        fields = ['airport', 'runway_number', 'length', 'width']
        read_only_fields = ['id']
