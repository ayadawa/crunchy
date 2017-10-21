from django.db import models
from django.contrib.auth.models import User
from hotels.models import Hotel


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return "%s in %s from %s - %s" % (self.user.username, self.hotel.name, self.start_date, self.end_date)

