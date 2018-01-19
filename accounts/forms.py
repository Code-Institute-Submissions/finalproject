from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import UserProfile


class UserLoginForm(forms.Form):
    """
    Used by the user to enter login credentials
    """
    username_or_email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """
    Used by the user to sign up with the website
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password Confirmation',
        widget=forms.PasswordInput
    )
    date_of_birth = forms.CharField(max_length=30)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'date_of_birth']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email addresses must be unique.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise ValidationError("Password must not be empty")

        if password1 != password2:
            raise ValidationError("Passwords do not match")

        return password2
        
class StartASub(forms.Form):

    MONTH_CHOICES = [(i, i,) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i,) for i in range(2018, 2036)]

    credit_card_number = forms.CharField(label='Credit card number', required=False)
    cvv = forms.CharField(label='Security code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
    
    
class PersonalSubform(forms.Form):
        STYLE_CHOICES = (
                ("Casual", "Casual"),
                ("Sport", "Sport"),
                ("Business", "Business"),
                ("Formal", "Formal"),
                ("Mix it up", "Mix it up")
                )
        styles = forms.ChoiceField(choices=STYLE_CHOICES)
        GENDER_CHOICES = (
                ("Male", "Male"),
                ("Female", "Female"),
                ("Other", "Other")
            )
            
        gender =forms.ChoiceField( choices=GENDER_CHOICES)
        
        height_CM = forms.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(300)])
                                       
        waist_IN = forms.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])
                                       
        shoesize = forms.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(20)])
        
        frontpic = forms.ImageField()
        sidepic = forms.ImageField()
        
        budget = forms.IntegerField()
        favourite_brands = forms.CharField(widget=forms.Textarea)
        
        class Meta:
            fields = ['Choose Style', 'Gender', 'Height (cm)', 'Waist (in)', 'Shoe Size', 'Front Profile Image', 'Side Profile Image', 'Budget €', 'Favourite Brands']
            
        
class UpdateNeeds(forms.Form):
        STYLE_CHOICES = (
                ("Casual", "Casual"),
                ("Sport", "Sport"),
                ("Business", "Business"),
                ("Formal", "Formal"),
                ("Mix it up", "Mix it up")
                )
        styles = forms.ChoiceField(choices=STYLE_CHOICES)
        waist_IN = forms.IntegerField(validators=[MinValueValidator(0),
                                       MaxValueValidator(100)])
        frontpic = forms.ImageField()
        sidepic = forms.ImageField()
        
        budget = forms.IntegerField()
        favourite_brands = forms.CharField(widget=forms.Textarea)
        
        class Meta:
            fields = ['Choose Style', 'Waist (in)', 'Front Profile Image', 'Side Profile Image', 'Budget €', 'Favourite Brands']
            
            
class PhotoForm(forms.Form):
    class Meta:
        model= UserProfile
        fields=('image')
        
    updatepic = forms.ImageField('image')
    
    def clean_photo(self):
        photo=self.cleaned_data.get('image')
        if photo.size>settings.MAX_UPLOAD_SIZE:
            raise forms.ValidationError(_("Whoa there! Please upload a smaller image!".format(str(settings.MAX_UPLOAD_SIZE/1000000))))
        return photo
        
class ContactForm(forms.Form):
    name = forms.CharField()
    email =  forms.CharField()
    issue = forms.CharField(widget=forms.Textarea)