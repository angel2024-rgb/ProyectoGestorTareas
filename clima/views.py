from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from rest_framework.permissions import AllowAny

class ClimaView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        # Ubicación de Lima
        latitude = float(request.query_params.get("latitude", -12.0432))   
        longitude = float(request.query_params.get("longitude", -77.0282))

        # Llamada a la API de Open-Meteo
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m",
            "timezone": "auto",
            "forecast_hours": 1,
            "past_hours": 1
        }
        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            ultima_temperatura = data["hourly"]["temperature_2m"][-1]
            hora = data["hourly"]["time"][-1]
            resultado = {
                "hora": hora,
                "temperatura": ultima_temperatura
            }
            return Response(resultado)
        else:
            return Response({"error": "No se pudo obtener el clima"}, status=response.status_code)