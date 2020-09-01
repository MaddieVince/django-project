from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'biography', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class':'form-control', 'placeholder':'Select your birthday', 'type':'date'}),
        }
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']