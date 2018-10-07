from django.db import models


class Customer(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    pwd = models.CharField(max_length=100)
    mn = models.BigIntegerField()

    def __str__(self):
        return self.fname