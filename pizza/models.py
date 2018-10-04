from django.db import models

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    small = models.DecimalField(2)
    large = models.DecimalField(2)

class Toppings(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(2)