from django.db import models
import os
import random
from django.db.models import Q
from core.utils import unique_slug_generator, upload_image_path
from django.db.models.signals import pre_save, post_save
from django.urls import reverse



class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(Q(featured=True) & Q(active=True))

    def search(self, query):
        lookups = (Q(title__icontains=query)|
                   Q(description__icontains=query)|
                   Q(price__icontains=query)|
                   Q(tag__title__icontains=query))
        return self.filter(lookups).distinct()    


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def all(self):
        return self.get_queryset().active()
    
    def featured(self):
        return self.get_queryset().featured()
    
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count()==1:
            return qs.first()
        return None
    
    def search(self, query):
        return self.get_queryset().active().search(query)


class Product(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    slug = models.SlugField(blank=True,unique=True)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return reverse("products:detail", kwargs={'slug':self.slug})
    
    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return self.title
    
    @property
    def name(self):
        return self.title


def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
    
pre_save.connect(product_pre_save_receiver, sender=Product)

