from django.db import models
from django.contrib.auth.models import User

class shopping_model(models.Model):
    image = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = models.TextField()


class myBasket_model(models.Model):
    product = models.ForeignKey(shopping_model, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class myFavorite_model(models.Model):
    product = models.ForeignKey(shopping_model, on_delete=models.CASCADE)



    


