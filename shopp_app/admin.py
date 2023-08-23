from django.contrib import admin
from .models import shopping_model, myBasket_model, myFavorite_model

class shopping_model_view(admin.ModelAdmin):
    list_display = ('title',)

class MyBasketAdmin(admin.ModelAdmin):
    list_display = ('product_title', 'quantity')

    def product_title(self, obj):
        return obj.product.title
    
class myFavoriteAdmin(admin.ModelAdmin):
    list_display = ('product_title',)

    def product_title(self, obj):
        return obj.product.title

admin.site.register(shopping_model, shopping_model_view)
admin.site.register(myBasket_model, MyBasketAdmin)
admin.site.register(myFavorite_model, myFavoriteAdmin)