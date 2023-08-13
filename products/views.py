from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from django.http import Http404




class ProductFeaturedListView(ListView):
    template_name = 'products/products.html'
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all().featured()


class ProductFeaturedDetailView(DetailView):
    queryset = Product.objects.all().featured()
    template_name = 'products/featured_detail.html'


class ProductListView(ListView):
    template_name = 'products/products.html'
    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.all()



class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs['slug']
        try:
            instance = Product.objects.get(slug=slug, active=True)
        except Product.DoesNotExist:
            raise Http404("Not found")
        except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404('oopss')
        return instance


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/product_detail.html'

    def get_context_data(self, *args,**kwargs):
        context =  super(ProductDetailView, self).get_context_data(*args ,**kwargs)
        return context
    
    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(id=pk)
        if instance is None:
            raise Http404("product doesnt exist")
        return instance

