from django.db import models
from django.contrib.auth.models import User
from hotels.models import Hotel


class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE)
    start_date = models.DateTimeField()
    start_end = models.DateTimeField()


