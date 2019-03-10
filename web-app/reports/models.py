import datetime

from django.db import models
from django.utils import timezone

class Report(models.Model):
    transcript = models.CharField(max_length=20000)
    pub_date = models.DateTimeField('date published')
    gps_lat = models.DecimalField(max_digits=9, decimal_places=6)
    gps_long = models.DecimalField(max_digits=9, decimal_places=6)
    moving = models.BooleanField()
