from django.db import models

class Person(models.Model):
    title = models.CharField(max_length=10, choices=[('Dr.', 'Dr.'), ('Rep.', 'Rep.')])

