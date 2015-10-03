from django import forms

from .models import Person,Cloth

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        widgets={
        'password':forms.PasswordInput(),
        }
        fields=['first_name',
    'last_name',
    'user_name',
    'sex',
    'address',
    'email_id',
    'phone_no',
    'secondary_phone_no',
    #'photos',
    'password',]

class LoginForm(forms.Form):
    login_id=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
    widgets={
    'password':forms.PasswordInput(),
    }

class ClothForm(forms.ModelForm):
    class Meta:
        model=Cloth
        fields=[
        'cloth_type',
        'catagory',
        'color',
        'brand',
        'material',
        'status',
        'cost',
        ]
