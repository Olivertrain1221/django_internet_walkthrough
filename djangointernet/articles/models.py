from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    # add in thumbnail later
    # also add in author later
