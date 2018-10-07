from django.db import models

# Create your models here.

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    small = models.DecimalField(max_digits=5, decimal_places=2)
    large = models.DecimalField(max_digits=5, decimal_places=2)
    ToppingCost = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    # fk_toppings = models.ForeignKey('Toppings', on_delete=models.PROTECT, related_name="toppings")

    def __str__(self):
        return f"{self.pizza_name} {self.category} {self.small} {self.large} {self.ToppingCost}"


class Toppings(models.Model):
    toppings_name = models.CharField(max_length=64)
    fk_pizza = models.ManyToManyField(Pizza, blank=True)

    def __str__(self):
        return f"{self.toppings_name}"


class Orders(models.Model):
    order_name = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    
    # Add timestamp to orders
    
    def __str__(self):
        return f"{self.order_name} at {self.address}. Total ${self.total}"
    

#class OrderItems(models.Model):
#    fk_order = models.ForeignKey(Orders, on_delete=models.PROTECT)
#    fk_pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT)
#    ItemPrice = models.DecimalField(max_digits=5, decimal_places=2)
#
#    def __str__(self):
#        return f"{self.fk_order} - {self.fk_pizza} {self.ItemPrice}"