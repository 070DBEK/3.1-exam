from django.urls import path
from .views import TemperatureAvgView, TemperatureMinView, TemperatureMaxView


urlpatterns = [
    path('temperature-avg/', TemperatureAvgView.as_view(), name='temperature-avg'),
    path('temperature-min/', TemperatureMinView.as_view(), name='temperature-min'),
    path('temperature-max/', TemperatureMaxView.as_view(), name='temperature-max'),
]
