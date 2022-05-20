from django.db import models

class user(models.Model):
    access_token = models.CharField(max_length=500)
    name = models.CharField(max_length=1000)
    popularity = models.CharField(max_length=1000)
    interpret = models.CharField(max_length=1000)
