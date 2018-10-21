from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Pizza model
class Pizza(models.Model):
    pizza_name = models.CharField(max_length=64)
    category = models.CharField(max_length=64)
    small = models.IntegerField()
    large = models.IntegerField()
    ToppingCost = models.IntegerField(null=True)
    # fk_toppings = models.ForeignKey('Toppings', on_delete=models.CASCADE, related_name="toppings")
    
    class Meta:
        verbose_name = "pizza"
        verbose_name_plural = "pizzas"

    def __str__(self):
        return f"{self.pizza_name} {self.category} {self.small} {self.large} {self.ToppingCost}"

# Toppings options
class Toppings(models.Model):
    toppings_name = models.CharField(max_length=64)
    fk_pizza = models.ManyToManyField(Pizza, blank=True)

    def __str__(self):
        return f"{self.toppings_name}"

    class Meta:
        verbose_name = "topping"
        verbose_name_plural = "toppings"

# Holds Orders 
class Orders(models.Model):
    fk_User = models.ForeignKey(User, related_name = "customer", on_delete = models.CASCADE)
    address = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip = models.CharField(max_length=5)
    total = models.DecimalField(max_digits=5, decimal_places=2)
    # created_on = models.DateField(auto_now_add=True)

    # Add timestamp to orders

    def __str__(self):
        return f"{self.order_name} at {self.address}. Total ${self.total}"

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"


class OrderItems(models.Model):
    fk_order = models.ForeignKey(Orders, related_name = "items", on_delete = models.CASCADE)
    fk_pizza = models.ForeignKey(Pizza, on_delete = models.CASCADE)
    toppings = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.fk_order} - {self.fk_pizza} {self.ItemPrice}"
    
    def get_cost(self):
        return self.price * self.quantity