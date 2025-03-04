from django.urls import path
from .views import *


urlpatterns = [
    path('weather-data/', WeatherDataListCreateView.as_view(), name='weather-list'),
    path('weather-data/<int:pk>/', WeatherDataDetailView.as_view(), name='weather-detail'),
    path('weather-data/location/<int:location_id>/', WeatherDataByLocationView.as_view(),name='weather-data-by-location'),

    path('forecast/', ForecastListCreateView.as_view(), name='forecast-list'),
    path('forecast/<int:pk>/', ForecastDetailView.as_view(), name='forecast-detail'),
]
