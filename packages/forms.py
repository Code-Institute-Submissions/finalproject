from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class PackageForm(forms.Form):
        STYLE_CHOICES = (
                ("Casual", "Casual"),
                ("Sport", "Sport"),
                ("Business", "Business"),
                ("Formal", "Formal"),
                ("All the above", "All the above")
                )
        styles = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                             choices=STYLE_CHOICES)
        GENDER_CHOICES = (
                ("Male", "Male"),
                ("Female", "Female"),
                ("Other", "Other")
            )
            
        gender = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=GENDER_CHOICES)
        
        height = forms.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(300)])
                                       
        waist = forms.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])
                                       
        shoesize = forms.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(20)])
        
        frontpic = forms.ImageField()
        sidepic = forms.ImageField()
        
        class Meta:
            fields = ['Choose Style', 'Gender', 'Height', 'Waist', 'Shoe Size', 'Front Profile Image', 'Side Profile Image']
            
            

        