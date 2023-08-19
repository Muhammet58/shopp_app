from django.shortcuts import render, get_object_or_404, redirect
from .models import shopping_model, myBasket_model

def homePage(request):
    data = {
        "shopping_model": shopping_model.objects.all(),
    }
    return render(request, "shopp_app/homePage.html", data)



def add_to_mybasket(request, product_id):
    get_to_product = get_object_or_404(shopping_model, id=product_id)
    basket, created = myBasket_model.objects.get_or_create(product=get_to_product, defaults={'quantity': 1})

    if not created:
        basket.quantity += 1 
        basket.save()

    return redirect('shoppingPage')




def shoppingPage(request):
     baskets = myBasket_model.objects.all() 
     total_price = sum(item.product.price * item.quantity for item in baskets)

     context = {
        'baskets': baskets,
        'total_price': total_price,
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

    return redirect('shoppingPage')

def decrease(request, product_id):
    to_decrease = get_object_or_404(myBasket_model, id=product_id)
    to_decrease.quantity -= 1
    to_decrease.save()

    return redirect('shoppingPage')

def remove(request, product_id):
    to_remove = get_object_or_404(myBasket_model, id=product_id)
    to_remove.delete()

    return redirect('shoppingPage')