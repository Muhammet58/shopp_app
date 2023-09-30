from django.contrib import admin
from .models import UserModel

class display(admin.ModelAdmin):
    list_display = ('username','is_superuser', 'is_staff', 'date_joined',)

admin.site.register(UserModel, display)
