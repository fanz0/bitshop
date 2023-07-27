from django.db import models
from django.conf import settings
from django.utils import timezone

class Tshirt(models.Model):
    quantity = models.IntegerField(default=1000)
    price = models.IntegerField(default=25)

class Hoodie(models.Model):
    quantity = models.IntegerField(default=1000)
    price = models.IntegerField(default=40)

