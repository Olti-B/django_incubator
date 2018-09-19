from django.db import models


class FarmesRegistraton(models.Model):

    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=25)
    date = models.DateTimeField()




