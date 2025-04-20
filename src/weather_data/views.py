from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
import io
from .models import WeatherRecord
from .serializers import WeatherRecordSerializer
from rest_framework import status

@method_decorator(csrf_exempt, name='dispatch')
class WeatherDataFileUpload(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({"message": "File is required"}, status=status.HTTP_400_BAD_REQUEST)

        decoded_file = io.TextIOWrapper(file.file, encoding='utf-8')
        df = pd.read_csv(decoded_file, sep=r'\s+', engine='python', na_values=["---"])
        df = df.dropna()
        df.columns = df.columns.str.strip()

        records = df.to_dict(orient='records')
        all_data = [
            WeatherRecord(
                year=record.get('year'),
                jan=record.get('jan'),
                feb=record.get('feb'),
                mar=record.get('mar'),
                apr=record.get('apr'),
                may=record.get('may'),
                jun=record.get('jun'),
                jul=record.get('jul'),
                aug=record.get('aug'),
                sep=record.get('sep'),
                oct=record.get('oct'),
                nov=record.get('nov'),
                dec=record.get('dec'),
                win=record.get('win'),
                spr=record.get('spr'),
                sum=record.get('sum'),
                aut=record.get('aut'),
                ann=record.get('ann'),
            )
            for record in records
        ]

        WeatherRecord.objects.bulk_create(all_data)
        return Response({"message": "Data uploaded successfully"}, status=status.HTTP_201_CREATED)


class GetWeatherData(APIView):
    def get(self, request):
        year = request.query_params.get('year')    

        if not year:
            return Response({"message": "Please Enter the year"}, status=status.HTTP_400_BAD_REQUEST)
           
        weather_data = WeatherRecord.objects.filter(year=year)
        
        if not weather_data.exists():
            return Response({"message": "Record not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serialize_data = WeatherRecordSerializer(weather_data, many=True)
        record = {
            "data": serialize_data.data,
            "successful": True,
            "status": status.HTTP_200_OK
        }

        return Response(record, status=status.HTTP_200_OK)
