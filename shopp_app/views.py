from django.shortcuts import render, get_object_or_404, redirect
from .models import shopping_model, myBasket_model, myFavorite_model
from account.models import addresses
from django.http import JsonResponse
from .forms import productAddForm
import urllib.parse


def homePage(request):
    busket_products = myBasket_model.objects.filter(user=request.user.id).values_list('product__id', flat=True)
    favorite_products = myFavorite_model.objects.filter(user=request.user.id).values_list('product__id', flat=True)
    user_baskets = myBasket_model.objects.filter(user=request.user)
    data = {
        "shopping_model": shopping_model.objects.all(),
        "busket_products": busket_products,
        "favorite_products": favorite_products,
        "baskets":user_baskets,
    }
    return render(request, "shopp_app/homePage.html", data)



def add_to_mybasket(request, product_id):
    get_to_product = get_object_or_404(shopping_model, id=product_id)
    basket, created = myBasket_model.objects.get_or_create(user=request.user, product=get_to_product, defaults={'quantity': 1})

    if not created:
        basket.quantity += 1 
        basket.save(commit=False)
        basket.user = request.user
        basket.save()
    else:
        message = "success"

    return JsonResponse({'message': message})



def shoppingPage(request):
     baskets = myBasket_model.objects.filter(user=request.user) 
     total_price = sum(item.product.price * item.quantity for item in baskets)
     favorites = myFavorite_model.objects.filter(user=request.user.id).values_list("product__id", flat=True)

     context = {
         'baskets': baskets,
         'total_price': total_price,
         'favorites': favorites,
         'address':addresses.objects.filter(userAddress=request.user)
         }
    
     return render(request, 'shopp_app/shoppingPage.html', context)



def buy_products(request):
    if request.method == "POST":
        myBasket_model.objects.filter(user=request.user).delete()

        info = {
            'info': 'Alışverişiniz başarılı bir şekilde tamamlanmıştır'
                }
        
        return render(request, 'shopp_app/shoppingPage.html', info)
          


def increase(request, product_id):
    to_increase = get_object_or_404(myBasket_model, user=request.user, id=product_id)
    to_increase.quantity += 1
    to_increase.save()

    baskets = myBasket_model.objects.filter(user=request.user)
    total_price =  sum(item.quantity * item.product.price for item in baskets)

    return JsonResponse({"new_quantity": to_increase.quantity, "new_total_price": total_price})



def decrease(request, product_id):
    to_decrease = get_object_or_404(myBasket_model, user=request.user, id=product_id)
    if to_decrease.quantity > 1:
        to_decrease.quantity -= 1
        to_decrease.save()

    baskets = myBasket_model.objects.filter(user=request.user)
    total_price =  sum(item.quantity * item.product.price for item in baskets)

    return JsonResponse({"new_quantity": to_decrease.quantity, "new_total_price": total_price})



def remove(request, product_id):
    to_remove = get_object_or_404(myBasket_model, user=request.user, id=product_id)
    to_remove.delete()

    basket = myBasket_model.objects.filter(user=request.user)
    total_price = sum(item.quantity * item.product.price for item in basket)
    item_quantity = myBasket_model.objects.count()

    return JsonResponse({"message": "deleted", "new_total_price": total_price, "warning":"Sepetinizde ürün bulunmamaktadır", "item_quantity":item_quantity })



def myFavorite(request):
    myFavorite = myFavorite_model.objects.filter(user=request.user)
    basket_product = myBasket_model.objects.filter(user=request.user.id).values_list('product__id', flat=True)
    data = {
        'myFavorite': myFavorite,
        'basket_product':basket_product
    }
    return render(request, 'shopp_app/myFavorites.html', data)



def add_to_favorite(request, product_id):
    product = get_object_or_404(shopping_model, id=product_id)
    favorite, created = myFavorite_model.objects.get_or_create(user=request.user, product=product)

    if not created:
        favorite.delete()
        message = "removed"
    else:
        message = "added"

    return JsonResponse({'message': message})



def remove_from_favorite(request, product_id):
    favorite = get_object_or_404(myFavorite_model, user=request.user, product_id=product_id)
    favorite.delete()

    item_quantity = myFavorite_model.objects.count()

    return JsonResponse({"message": "deleted", "item_quantity":item_quantity})



def product_add(request):
    if request.user.is_superuser and request.user.is_authenticated:
        if request.method == 'POST':
            item = productAddForm(request.POST, request.FILES)

            if item.is_valid:
                item.save()

                return redirect("homePage")
                
        form = productAddForm()
        return render(request, 'shopp_app/product_add.html', {'form':form})



def product_remove_page(request):
    if request.user.is_superuser and request.user.is_authenticated:
        data = {
            "shopping_model":shopping_model.objects.all(),
                            }
        return render(request, 'shopp_app/product_remove.html', data)
    


def product_remove(request, id):
    if request.user.is_superuser and request.user.is_authenticated:
        item = get_object_or_404(shopping_model, id=id)
        item.delete()

        item_quantity = shopping_model.objects.count()

        return JsonResponse({"message":"deleted", "item_quantity":item_quantity})
                    
   

def address(request):
    selected_address = request.GET.get('selected_address')
    request.user.address = selected_address
    request.user.save()
    return JsonResponse({"message": "success", "new_address": selected_address})



def quantity_increase(request, title):
    new_title = urllib.parse.unquote(title)
    increase = get_object_or_404(myBasket_model, user=request.user, product__title=new_title)
    increase.quantity += 1
    increase.save()

    return JsonResponse({"increased_amount": increase.quantity})

def quantity_decrease(request, title):
    increase = get_object_or_404(myBasket_model, user=request.user, product__title=title)
    
    if increase.quantity > 1:
        increase.quantity -= 1
        increase.save()

    return JsonResponse({"decreased_amount": increase.quantity})
