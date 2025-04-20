from django.urls import path
from .views import WeatherDataFileUpload,GetWeatherData

urlpatterns = [
    path('WeatherDataFileUpload', WeatherDataFileUpload.as_view(), name='WeatherDataFileUpload'),
    path('GetWeatherData',GetWeatherData.as_view(),name='GetWeatherData')
]
