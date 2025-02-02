from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Flights(models.Model):
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    duration = models.IntegerField()