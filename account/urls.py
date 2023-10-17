from django.urls import path
from . import views

urlpatterns = [
    path('login', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.Logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('change_address', views.change_address, name='change_address'),
    path('addAddress', views.addAddress, name='addAddress'),
    path('delete_address/<int:id>', views.delete_address, name='delete_address'),
]
