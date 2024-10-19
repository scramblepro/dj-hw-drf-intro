from rest_framework import generics
from .models import Sensor, TemperatureMeasurement
from .serializers import SensorSerializer, TemperatureMeasurementSerializer, SensorDetailInformationSerializer


class SensorListCreateView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class TemperatureMeasurementListCreateView(generics.ListCreateAPIView):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = TemperatureMeasurementSerializer


class SensorDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailInformationSerializer


class TemperatureMeasurementDetailView(generics.RetrieveDestroyAPIView):
    queryset = TemperatureMeasurement.objects.all()
    serializer_class = TemperatureMeasurementSerializer