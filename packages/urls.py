from django.conf.urls import url
from django.contrib import admin
from packages.views import get_packages, package_details

urlpatterns=[
    url(r'^$', get_packages, name="packagelist"),
    url(r'^(\d+)$', package_details, name="packagedeets"),
    ]