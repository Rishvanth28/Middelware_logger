from rest_framework import serializers
from .models import ShortURL

class ShortURLSerializer(serializers.ModelSerializer):
    shortLink = serializers.SerializerMethodField()
    expiry = serializers.SerializerMethodField()

    class Meta:
        model = ShortURL
        fields = ['original_url', 'shortcode', 'shortLink', 'expiry']

    def get_shortLink(self, obj):
        request = self.context.get('request')
        return f"{request.scheme}://{request.get_host()}/{obj.shortcode}"

    def get_expiry(self, obj):
        return obj.expiry.isoformat()