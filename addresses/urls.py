from django.urls import path
from . import views


app_name = 'addresses'


urlpatterns = [
    path('', views.checkout_address_create_view, name='checkout_address_create')
]
