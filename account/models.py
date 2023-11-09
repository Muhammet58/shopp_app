from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    profile_photo = models.ImageField(upload_to="image")
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True, blank=True)
    address = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)


class addresses(models.Model):
    userAddress = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    city = models.CharField(max_length=200)
    county = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    street = models.CharField(max_length=255)
    number = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.city}/{self.county}/{self.district}/{self.street.replace(' ','&nbsp')}/{self.number}"
    
    class Meta:
        verbose_name = "adresler"
        verbose_name_plural = "adreslerim"



