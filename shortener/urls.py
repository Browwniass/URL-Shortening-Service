from django.urls import include, path
from rest_framework.routers import DefaultRouter

from shortener.views.shorteners import ShortenerView


urlpatterns = [
    path('shorten/', ShortenerView.as_view(), name='shortener_url') 
]