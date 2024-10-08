from django.contrib import admin

from shortener.models.shorteners import URLData


admin.site.register(URLData)
