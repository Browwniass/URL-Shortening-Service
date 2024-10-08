from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from shortener.serializers.shorteners import URLDataSerializer
from shortener.models.shorteners import URLData
from shortener.encodings import generate_short_url
from drf_spectacular.utils import extend_schema
from shortener.serializers.shorteners import URLDataSerializer


class ShortenerView(APIView):
    serializer_class = URLDataSerializer

    def post(self, request):
        serializer = URLDataSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            long_url = serializer.data
            existing_url = URLData.objects.filter(url=long_url).first()
            result_url = f'http://127.0.0.1:8000/api/redirect/'
            if existing_url:
                short_url = URLDataSerializer(existing_url).data['short_url']
                return Response(result_url+short_url, status=status.HTTP_200_OK)
            
            url = URLData.objects.create(url=long_url)
            short_url = generate_short_url(url.id)
            url.short_url=short_url
            url.save()
            return Response(result_url+short_url, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


