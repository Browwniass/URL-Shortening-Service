from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponseRedirect
from drf_spectacular.utils import extend_schema, extend_schema_view

from shortener.serializers.shorteners import URLDataSerializer
from shortener.models.shorteners import URLData
from shortener.encodings import generate_short_url
from shortener.serializers.shorteners import URLDataSerializer


@extend_schema_view(
    post=extend_schema(summary='Сокращение URL', tags=['Сокращатель_URL']),
)
class ShortenerView(APIView):
    serializer_class = URLDataSerializer

    def post(self, request):
        serializer = URLDataSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            long_url = serializer.data['url']
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


@extend_schema_view(
    get=extend_schema(summary='Перенаправка по сокращенному URL', tags=['Сокращатель_URL']),
)
class RedirectView(APIView):
    def get(self, request, subpath):
        url_data  = URLData.objects.filter(short_url=subpath).first()
        if url_data is not None:
            redirect_url = getattr(url_data , 'url')
            return HttpResponseRedirect(redirect_url)
        return Response({'error': 'URL not found'}, status=status.HTTP_404_NOT_FOUND)
