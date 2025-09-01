from .logger import Log
import time

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        Log("backend", "info", "middleware", f"Request started: {request.method} {request.path}")

        start_time = time.time()
        try:
            response = self.get_response(request)
        except Exception as e:

            Log("backend", "error", "middleware", f"Exception: {str(e)}")
            raise

        duration = (time.time() - start_time) * 1000
        Log("backend", "info", "middleware", f"Request completed: {request.method} {request.path} in {duration:.2f}ms")

        return response