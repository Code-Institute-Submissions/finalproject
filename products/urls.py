from django.conf.urls import url, include
from django.contrib import admin
from products.views import get_products, do_search, product_details, add_review, show_category

urlpatterns=[
    url(r'^$', get_products, name="productlist"),
    url(r'^search/', do_search, name="search"),
    url(r'^(\d+)$', product_details, name='product_details'),
    url(r'^(\d+)/review/add$', add_review, name="add_review"),
    url(r'^category/(?P<hierarchy>.+)/$', show_category, name='category'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    ]