from rest_framework import generics
from locations.pagination import CustomPagination
from . import models
from .serializers import WeatherDataSerializer, ForecastSerializer


class WeatherDataListCreateView(generics.ListCreateAPIView):
    queryset = models.WeatherData.objects.all()
    serializer_class = WeatherDataSerializer
    pagination_class = CustomPagination


class WeatherDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.WeatherData.objects.all()
    serializer_class = WeatherDataSerializer


class WeatherDataByLocationView(generics.ListAPIView):
    serializer_class = WeatherDataSerializer

    def get_queryset(self):
        location_id = self.kwargs['location_id']
        return models.WeatherData.objects.filter(location_id=location_id)



class ForecastListCreateView(generics.ListCreateAPIView):
    queryset = models.Forecast.objects.all()
    serializer_class = ForecastSerializer
    pagination_class = CustomPagination


class ForecastDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Forecast.objects.all()
    serializer_class = ForecastSerializer