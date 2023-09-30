from django.db import models
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True, blank=True)
    address = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)



