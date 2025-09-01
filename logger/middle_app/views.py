from django.http import JsonResponse
from .logger import Log

def test_view(request):
    Log("backend", "debug", "handler", "test_view triggered")
    return JsonResponse({"message": "Logging middleware works!"})