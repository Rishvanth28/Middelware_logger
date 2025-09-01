from django.urls import path
from .views import CreateShortURL, ShortURLStats

urlpatterns = [
    path("shorturls", CreateShortURL.as_view()),
    path("shorturls/<str:shortcode>", ShortURLStats.as_view()),
]