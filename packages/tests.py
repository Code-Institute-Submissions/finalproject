from django.test import TestCase
from .models import Packages

# Create your tests here.
class PackageTests(TestCase):
    
    def test_str(self):
        test_name = Packages(name='A package')
        self.assertEqual(str(test_name), 'A package')

