from django.shortcuts import render, get_object_or_404, redirect
from .models import shopping_model, myBasket_model, myFavorite_model
from django.http import JsonResponse

def homePage(request):
    data = {
        "shopping_model": shopping_model.objects.all(),
        "busket_products": myBasket_model.objects.filter().values_list('product__id', flat=True),
        "favorite_products": myFavorite_model.objects.filter().values_list('product__id', flat=True),
    }
    return render(request, "shopp_app/homePage.html", data)



def add_to_mybasket(request, product_id):
    get_to_product = get_object_or_404(shopping_model, id=product_id)
    basket, created = myBasket_model.objects.get_or_create(product=get_to_product, defaults={'quantity': 1})

    if not created:
        basket.quantity += 1 
        basket.save()

    return JsonResponse({'message': not created})



def shoppingPage(request):
     baskets = myBasket_model.objects.all() 
     total_price = sum(item.product.price * item.quantity for item in baskets)
        

     context = {
         'baskets': baskets,
         'total_price': total_price
         }
    
     return render(request, 'shopp_app/shoppingPage.html', context)



def buy_products(request):
    if request.method == "POST":
        myBasket_model.objects.all().delete()

        info = {
            'info':'Alışverişiniz başarılı bir şekilde tamamlanmıştır'
        }

        return render(request, 'shopp_app/shoppingPage.html', info)
    


def increase(request, product_id):
    to_increase = get_object_or_404(myBasket_model, id=product_id)
    to_increase.quantity += 1
    to_increase.save()

    baskets = myBasket_model.objects.all()
    total_price =  sum(item.quantity * item.product.price for item in baskets)

    return JsonResponse({"new_quantity": to_increase.quantity, "new_total_price": total_price})



def decrease(request, product_id):
    to_decrease = get_object_or_404(myBasket_model, id=product_id)
    to_decrease.quantity -= 1
    to_decrease.save()

    baskets = myBasket_model.objects.all()
    total_price =  sum(item.quantity * item.product.price for item in baskets)

    return JsonResponse({"new_quantity": to_decrease.quantity, "new_total_price": total_price})



def remove(request, product_id):
    to_remove = get_object_or_404(myBasket_model, id=product_id)
    to_remove.delete()

    basket = myBasket_model.objects.all()
    total_price = sum(item.quantity * item.product.price for item in basket)

    return JsonResponse({"message": "deleted", "new_total_price": total_price, })



def myFavorite(request):
    myFavorite = myFavorite_model.objects.all()
    data = {
        'myFavorite': myFavorite
    }
    return render(request, 'shopp_app/myFavorites.html', data)



def add_to_favorite(request, product_id):
    product = get_object_or_404(shopping_model, id=product_id)
    favorite, created = myFavorite_model.objects.get_or_create(product=product)

    if not created:
        favorite.delete()

    return JsonResponse({'message': not created})



def remove_from_favorite(request, product_id):
    favorite = get_object_or_404(myFavorite_model, product_id=product_id)
    favorite.delete()
    return JsonResponse({"message": "deleted"})





        