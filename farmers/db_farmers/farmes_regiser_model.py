from django.utils import timezone
from django.db import models
from incubator import settings


class FarmesRegistraton(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    id_reg_farmer = models.CharField(max_length=10, default='notset')
    phone_number = models.IntegerField()
    city = models.CharField(max_length=25)
    date = models.DateTimeField(timezone.now())


class SoldProduct(models.Model):
    date = models.DateTimeField(timezone.now())


class PostProduct(models.Model):
    title = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    description = models.CharField(max_length=225)
    content = models.CharField(max_length=225)
    image = models.ImageField(upload_to='farmers_post', blank=True)
    date = models.DateTimeField(timezone.now())
