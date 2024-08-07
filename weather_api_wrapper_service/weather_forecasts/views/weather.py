"""Weather views."""

# Django
# Utilities
import requests
from django.conf import settings
from django.core.cache import cache

# Django REST Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
from weather_api_wrapper_service.weather_forecasts.serializers import WeatherSerializer


class WeatherByPostalCodeView(APIView):
    """Search weather by postal code."""

    def post(self, request, *args, **kwargs):
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            postal_code = serializer.validated_data["postal_code"]
            cache_key = f"weather_{postal_code}"
            weather_data = cache.get(cache_key)

            if not weather_data:
                api_key = settings.OPENWEATHERMAP_API_KEY
                url = f"http://api.openweathermap.org/data/2.5/weather?zip={postal_code},AR&appid={api_key}&units=metric"
                response = requests.get(url)

                if response.status_code == 200:
                    weather_data = response.json()
                    cache.set(cache_key, weather_data, timeout=3600)
                else:
                    return Response(
                        {"error": "Unable to fetch weather data"},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    )

            return Response(weather_data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
