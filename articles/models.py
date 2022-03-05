from django.db import models


class Article(models.Model):
    title = models.CharField()
    content = models.TextField()
