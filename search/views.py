from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView
from products.models import Product




class SearchProductView(ListView):
    template_name = 'search/search.html'

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET['q']
        context['query'] = query
        return context
    
    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None)
        if query is not None:
            return Product.objects.search(query)
        return Product.objects.featured()
    