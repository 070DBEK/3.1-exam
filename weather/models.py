from django.db import models
from locations.models import Location


class WeatherData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.FloatField()
    precipitation = models.FloatField()
    recorded_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Weather Datas')



class Forecast(models.Model):
    forecast_date = models.DateField()
    temperature_min = models.FloatField()
    temperature_max = models.FloatField()
    humidity = models.FloatField()
    precipitation_probability = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='Forecast')

