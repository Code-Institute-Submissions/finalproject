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
            
            
class DynamicSub(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2018, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)