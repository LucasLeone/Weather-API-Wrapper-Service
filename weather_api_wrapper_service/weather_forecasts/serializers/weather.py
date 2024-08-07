"""Weather serializers."""

# Django REST Framework
from rest_framework import serializers


class WeatherSerializer(serializers.Serializer):
    """Weather serializer."""

    postal_code = serializers.CharField(max_length=10)
