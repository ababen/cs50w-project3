from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.name} {self.category}"


class Toppings(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    pizza = models.ManyToManyField(Pizza, blank=True, related_name="toppings")

    def __str__(self):
        return f"{self.name} {self.price}"


class Orders(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    total = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.id} - {self.name} at {self.address}. Total ${self.total}"


class OrderItems(models.Model):
    ForOrder = models.ForeignKey(Orders, on_delete=models.PROTECT, related_name="items")
    Item = models.ForeignKey(Pizza, on_delete=models.CASCADE, related_name="item")
    ItemPrice = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.Item} {self.ItemPrice}"