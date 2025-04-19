from django.urls import path
from .views import WeatherDataView

urlpatterns = [
    path('WeatherDataView', WeatherDataView.as_view(), name='WeatherDataView'),
]
