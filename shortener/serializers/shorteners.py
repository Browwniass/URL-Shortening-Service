from rest_framework import serializers
from shortener.models.shorteners import URLData


class URLDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLData
        fields = (
            'url', 
            'short_url',
        )
        read_only_fields = ('short_url',)
