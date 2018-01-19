# Create your models here.
from __future__ import unicode_literals
from django.db import models
from django.db.models import Avg
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from star_ratings.models import Rating


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    slug = models.SlugField()
    ratings = GenericRelation(Rating, related_query_name="products")
    
    @property
    def average_rating(self):
        rating = Review.objects.filter(product=self).aggregate(Avg('rating'))
        return rating['rating__avg']
    
        
    def __str__(self):
        return self.name 
    
        

    
class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images')
    image = models.ImageField(upload_to='images')
    
    def __str__(self):
        return str(self.image)
        
        
class Review(models.Model):
    author = models.ForeignKey('auth.User')
    product = models.ForeignKey(Product, related_name="reviews")
    title = models.CharField(max_length=200)
    content = models.TextField()
    rating = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
        
# class avgrating(models.Model):
#     average = Review.objects.all().aggregate(Avg('rating'))