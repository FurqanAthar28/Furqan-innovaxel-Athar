from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShortURL
from .serializers import ShortURLSerializer



"""Handles creation of short URLs via POST request"""

class ShortURLCreate(APIView):
    def post(self, request):
        # Deserialize incoming data
        serializer = ShortURLSerializer(data=request.data)
        # Validate and save if valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # Return validation errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Handles retrieval, update, and deletion of a short URL
class ShortURLDetail(APIView):

    # Retrieve the original URL and increment access count
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        # Increase the number of times this short URL has been accessed
        short_url.access_count += 1  # Track the number of times the url is accessed
        short_url.save()
        serializer = ShortURLSerializer(short_url)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # Replace the existing URL with new data
    def put(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        serializer = ShortURLSerializer(short_url, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Partially update (PATCH) an existing short URL
    def patch(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        serializer = ShortURLSerializer(short_url, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete a short URL by its short_code
    def delete(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        short_url.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Returns statistics for a specific short URL
class ShortURLStats(APIView):
    def get(self, request, short_code):
        short_url = get_object_or_404(ShortURL, short_code=short_code)
        return Response({
            "short_code": short_url.short_code,
            "original_url": short_url.url,
            "created_at": short_url.created_at,
            "updated_at": short_url.updated_at,
            "access_count": short_url.access_count,
        }, status=status.HTTP_200_OK)
