from rest_framework import serializers
from .models import ShortURL
class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortURL
        fields = '__all__'
        # These fields are auto-managed by the backend and should not be modified by the user
        read_only_fields = ['id', 'short_code', 'created_at', 'updated_at', 'access_count']
        