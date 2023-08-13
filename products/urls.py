from django.urls import path
from . import views



app_name = 'products'


urlpatterns = [
    path('list/', views.ProductListView.as_view(), name='list'),
    # path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='detail'),
    # path('featured-list/', views.ProductFeaturedListView.as_view(), name='featured-list'),
    # path('featured-detail/<int:pk>/', views.ProductFeaturedDetailView.as_view(), name='featured-detail'),
    path('detail/<slug:slug>/', views.ProductDetailSlugView.as_view(), name='detail'),
]
