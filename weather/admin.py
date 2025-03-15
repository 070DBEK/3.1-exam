from django.contrib import admin
from .models import WeatherData, Forecast


@admin.register(WeatherData)
class WeatherDataAdmin(admin.ModelAdmin):
    list_display = ('location', 'temperature', 'humidity', 'pressure', 'wind_speed', 'wind_direction', 'precipitation', 'recorded_at')
    search_fields = ('location__name',)
    list_filter = ('recorded_at', 'location')
    ordering = ('-recorded_at',)


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('location', 'forecast_date', 'temperature_min', 'temperature_max', 'humidity', 'precipitation_probability', 'wind_speed', 'wind_direction', 'created_at')
    search_fields = ('location__name',)
    list_filter = ('forecast_date', 'location')
    ordering = ('-forecast_date',)
