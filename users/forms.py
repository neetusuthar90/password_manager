from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import User

class RegistrationForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password','style':'width: 1000px'}),label='')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password','style':'width: 1000px'}),label='')
    
    class Meta:
        model = User
        fields = ["username", "email", "password"]

        labels = {
            'username':'',
            'email':'',
        }
        widgets = {
            "username": forms.TextInput(attrs={'class':'form-control','placeholder':'Username', 'style':'width: 1000px'}),
            "email": forms.EmailInput(attrs={'class':'form-control','placeholder':'Email Address','style':'width: 1000px'}),
        }
    

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Password And Confirm Password Does Not Match!!")

        return cleaned_data

