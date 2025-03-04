from django.db.models import Avg, Max, Min
from rest_framework.response import Response
from rest_framework.views import APIView
from weather.models import WeatherData


class TemperatureAvgView(APIView):
    def get(self, request):
        avg_temp = WeatherData.objects.aggregate(Avg('temperature'))['temperature__avg']
        return Response({"average_temperature": avg_temp})


class TemperatureMinView(APIView):
    def get(self, request):
        min_temp = WeatherData.objects.aggregate(Min('temperature'))['temperature__min']
        return Response({"min_temperature": min_temp})


class TemperatureMaxView(APIView):
    def get(self, request):
        max_temp = WeatherData.objects.aggregate(Max('temperature'))['temperature__max']
        return Response({"max_temperature": max_temp})
