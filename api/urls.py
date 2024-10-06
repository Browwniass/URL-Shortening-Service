from django.urls import path, include

from shortener.urls import urlpatterns as shortener_urls


app_name = 'api'

urlpatterns = [
]

urlpatterns += shortener_urls
