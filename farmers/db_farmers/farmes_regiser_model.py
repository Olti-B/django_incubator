from django.utils import timezone

from django.db import models


class FarmesRegistraton(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    id_reg_farmer = models.CharField(max_length=10, default='notset')
    phone_number = models.IntegerField()
    city = models.CharField(max_length=25)
    date = models.DateTimeField(timezone.now())


class SoldProducts(models.Model):
    date = models.DateTimeField(timezone.now())

class PostProducts(models.Model):
    date = models.DateTimeField(timezone.now())
