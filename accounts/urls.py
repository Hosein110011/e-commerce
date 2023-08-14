from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


app_name = 'accounts'


urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/guest/', views.guest_register_view, name='guest_register'),
]

