from django.db import models
from django.contrib.auth.models import User
from account.models import UserModel
from ckeditor.fields import RichTextField

class shopping_model(models.Model):
    image = models.ImageField(upload_to='image')
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    content = RichTextField(models.TextField())

    def save(self, *args, **kwargs):
        self.title = self.title.replace(" ", "_")
        super(shopping_model, self).save(*args, **kwargs)

class myBasket_model(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(shopping_model, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

class myFavorite_model(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    product = models.ForeignKey(shopping_model, on_delete=models.CASCADE)



    


