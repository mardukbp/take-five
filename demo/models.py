from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=255)


class Person(models.Model):
    name = models.CharField(max_length=255)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
