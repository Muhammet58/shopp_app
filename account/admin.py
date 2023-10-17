from django.contrib import admin
from .models import UserModel, addresses

class display(admin.ModelAdmin):
    list_display = ('username','is_superuser', 'is_staff', 'date_joined',)

class adressDisplay(admin.ModelAdmin):
    list_display = ('userAddress', 'city', 'county', 'district', 'street', 'number', 'date')

admin.site.register(UserModel, display)
admin.site.register(addresses, adressDisplay)
