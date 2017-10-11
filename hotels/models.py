from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    # expect a string with a delimiter of ','
    images = models.CharField(max_length=5000, null=True)

    def __str__(self):
        return self.name

    def images_as_list(self):
        return self.images.split(',')


