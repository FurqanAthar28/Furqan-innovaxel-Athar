from rest_framework import serializers
from .models import ShortURL
# Serializer to convert ShortURL model instances to and from JSON
class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        # Serializes all the fields
        fields = '__all__'

        