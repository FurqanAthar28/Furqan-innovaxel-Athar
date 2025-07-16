# shortener/urls.py
from django.urls import path
from .views import ShortURLCreate, ShortURLDetail, ShortURLStats

urlpatterns = [
    path('shorten', ShortURLCreate.as_view()),  # POST
    path('shorten/<str:short_code>', ShortURLDetail.as_view()),  # GET, PUT, PATCH, DELETE
    path('shorten/<str:short_code>/stats', ShortURLStats.as_view()),  # GET - stats
]
