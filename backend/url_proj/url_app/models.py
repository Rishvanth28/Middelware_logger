from django.db import models
from django.utils import timezone
import uuid

class ShortURL(models.Model):
    original_url = models.URLField()
    shortcode = models.CharField(max_length=20, unique=True, default=uuid.uuid4().hex[:6])
    created_at = models.DateTimeField(auto_now_add=True)
    validity = models.IntegerField(default=30)  # in minutes
    clicks = models.IntegerField(default=0)

    @property
    def expiry(self):
        return self.created_at + timezone.timedelta(minutes=self.validity)