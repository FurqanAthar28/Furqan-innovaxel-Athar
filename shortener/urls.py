# shortener/urls.py
from django.urls import path
from .views import ShortURLCreate, ShortURLDetail, ShortURLStats

urlpatterns = [
    # POST: Create a new short URL
    path('urls/', ShortURLCreate.as_view()),  # POST
    # GET: Retrieve original URL using short_code
    # PUT: Replace existing URL
    # PATCH: Partially update existing URL
    # DELETE: Delete short URL
    path('urls/<str:short_code>', ShortURLDetail.as_view()),  # GET, PUT, PATCH, DELETE
    path('urls/<str:short_code>/stats', ShortURLStats.as_view()),  # GET - stats
]

