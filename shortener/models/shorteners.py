from django.db import models


class URLData(models.Model):
    url = models.URLField('URL', unique=True)
    short_url = models.CharField(unique=True, blank=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.url}'