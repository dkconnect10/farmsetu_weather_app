from rest_framework.test import APITestCase
from django.urls import reverse
from .models import WeatherRecord

class WeatherDataAPITest(APITestCase):
    def setUp(self):
        WeatherRecord.objects.create(
            year=1886,
            jan=3.7, feb=3.4, mar=6.1, apr=10.5, may=13.1,
            jun=16.4, jul=18.7, aug=18.5, sep=16.0,
            oct=12.9, nov=8.6, dec=4.1,
            win=4.36, spr=9.88, sum=17.87, aut=12.51, ann=11.04
        )

    def test_get_weather_data_for_year(self):
        url = '/weather/GetWeatherData'
        response = self.client.get(url, {'year': 1886})

        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in response.data)
        self.assertEqual(response.data['data'][0]['year'], 1886)
