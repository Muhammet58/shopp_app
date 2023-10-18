from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('myBasket', views.shoppingPage, name="shoppingPage"),
    path('add_to_mybasket/<int:product_id>', views.add_to_mybasket, name="add_to_mybasket"),
    path('buy_products', views.buy_products, name="buy_products"),
    path('increase/<int:product_id>', views.increase, name="increase"),
    path('decrease/<int:product_id>', views.decrease, name="decrease"),
    path('remove/<int:product_id>', views.remove, name="remove"),
    path('my_favorite', views.myFavorite, name="my_favorite"),
    path('add_to_favorite/<int:product_id>', views.add_to_favorite, name="add_to_favorite"),
    path('remove_favorite_item/<int:product_id>', views.remove_from_favorite, name="remove_from_myFavorite"),
    path('product_add', views.product_add, name="product_add"),
    path('product_remove_page', views.product_remove_page, name="product_remove_page"),
    path('product_remove/<int:id>/', views.product_remove, name="product_remove"),
    path('address', views.address, name="address"),
]