from django.test import TestCase
from .models import Post
# Create your tests here.
class PostTests(TestCase):
    
    def test_str(self):
        test_title = Post(title='A blog')
        self.assertEqual(str(test_title), 'A blog')
