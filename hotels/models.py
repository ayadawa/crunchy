from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
