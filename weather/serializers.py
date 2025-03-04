from rest_framework import serializers
from .models import WeatherData, Forecast
from locations.models import Location
# from locations.serializers import LocationSerializer


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['id', 'name']



class WeatherDataSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = WeatherData
        fields = [
            'id',
            'location',
            'location_id',
            'temperature',
            'humidity',
            'pressure',
            'wind_speed',
            'wind_direction',
            'precipitation',
            'recorded_at'
        ]

    def create(self, validated_data):
        location = validated_data.pop('location_id', None)
        if not location:
            raise serializers.ValidationError("Location is required.")
        weather_data = WeatherData.objects.create(location=location, **validated_data)
        return weather_data

    def validate_temperature(self, value):
        if value < -100 or value > 100:
            raise serializers.ValidationError("Temperature must be between -100 and 100 degrees Celsius.")
        return value

    def validate(self, data):
        if 'temperature' in data and 'humidity' in data:
            if data['humidity'] < 0 or data['humidity'] > 100:
                raise serializers.ValidationError("Humidity must be between 0 and 100.")
        return data


class ForecastSerializer(serializers.ModelSerializer):
    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(
        queryset=Location.objects.all(), write_only=True, required=True
    )
    forecast_date = serializers.DateField(required=True)

    class Meta:
        model = Forecast
        fields = [
            'id',
            'location',
            'location_id',
            'forecast_date',
            'temperature_min',
            'temperature_max',
            'humidity',
            'precipitation_probability',
            'wind_speed',
            'wind_direction',
            'created_at'
        ]

    def create(self, validated_data):
        location = validated_data.pop('location_id')
        forecast = Forecast.objects.create(location=location, **validated_data)
        return forecast

    def validate(self, data):
        if data['temperature_min'] > data['temperature_max']:
            raise serializers.ValidationError("Minimum temperature cannot be higher than maximum temperature.")
        if data['humidity'] < 0 or data['humidity'] > 100:
            raise serializers.ValidationError("Humidity must be between 0 and 100.")
        return data
