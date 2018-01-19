
from django.test import TestCase

from .views import view_cart
from django.core.urlresolvers import resolve
 
class CartTest(TestCase):
    def test_cart_resolves(self):
        cart_page = resolve('/cart/')
        self.assertEqual(cart_page.func, view_cart)