from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    """
    Serializer for the ShortURL model.
    Handles validation and conversion between model instances and JSON.
    """

    def validate_url(self, value):
        """
        Ensure the URL starts with http or https.
        """
        if not value.startswith("http"):
            raise serializers.ValidationError("URL must start with http or https.")
        return value

    class Meta:
        model = ShortURL
        fields = '__all__'
