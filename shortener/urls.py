from django.urls import include, path
from rest_framework.routers import DefaultRouter

from shortener.views.shorteners import ShortenerView, RedirectView


urlpatterns = [
    path('shorten/', ShortenerView.as_view(), name='shortener_url'),
    path('redirect/<str:subpath>/', RedirectView.as_view(), name='redirect_url'),
]