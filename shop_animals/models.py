
from django.db import models
from django.conf import settings

class Animal(models.Model):
    name = models.CharField(max_length=150)
    species = models.CharField(max_length=100)
    age = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='animals/')

    def __str__(self):
        return self.name
