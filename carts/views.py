from django.shortcuts import render, redirect
from .models import Cart
from products.models import Product
from django.contrib import messages


def cart_home(request):
    cart_obj , new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
    cart_obj.total = total
    cart_obj.save()
    return render(request, 'carts/cart_home.html', {'cart':cart_obj})


def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            messages.error(request, "product is not found")
            return redirect('carts:cart-home')
        cart_obj , new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
    return redirect('carts:cart-home')
    








