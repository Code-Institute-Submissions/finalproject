from django import forms
from .models import Review

class ProductReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'content')
        
    CHOICES = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    ]
    rating = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    
