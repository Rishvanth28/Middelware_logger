from rest_framework import generics
from rest_framework.response import Response
from .models import ShortURL
from .serializers import ShortURLSerializer
from django.shortcuts import get_object_or_404

class CreateShortURL(generics.CreateAPIView):
    serializer_class = ShortURLSerializer

class ShortURLStats(generics.RetrieveAPIView):
    serializer_class = ShortURLSerializer
    lookup_field = 'shortcode'
    queryset = ShortURL.objects.all()