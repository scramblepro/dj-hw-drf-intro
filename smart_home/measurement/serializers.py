from rest_framework import serializers
from .models import Sensor, TemperatureMeasurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = '__all__'


class TemperatureMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemperatureMeasurement
        fields = '__all__'


class SensorDetailInformationSerializer(serializers.ModelSerializer):
    measurements = TemperatureMeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'latitude', 'created_at', 'updated_at', 'measurements']