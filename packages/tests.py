from django.test import TestCase
from .models import Package

# Create your tests here.
class PackageTests(TestCase):
    
    def test_str(self):
        test_name = Package(name='A package')
        self.assertEqual(str(test_name), 'A package')

