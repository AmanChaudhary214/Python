from django.db import models

class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Order(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    status = models.CharField(max_length=50, default='received')

    def __str__(self):
        return f"{self.customer_name} - {self.dish}"
