from django.urls import path
from . import views


app_name = 'carts'


urlpatterns = [
    path('', views.cart_home, name='cart-home'),
    path('cart-update/', views.cart_update, name='cart-update'),
    path('checkout/', views.checkout_home, name='checkout'),
]
