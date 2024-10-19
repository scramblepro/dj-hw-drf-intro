from django.urls import path
from .views import SensorListCreateView, TemperatureMeasurementListCreateView, SensorDetailUpdateView, TemperatureMeasurementDetailView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorDetailUpdateView.as_view(), name='sensor-detail-update'),
    path('measurements/', TemperatureMeasurementListCreateView.as_view(), name='measurement-list-create'),
    path('measurements/<int:pk>/', TemperatureMeasurementDetailView.as_view(), name='measurement-detail'),
]