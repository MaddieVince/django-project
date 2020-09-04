from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm
)
from .models import CustomUser

author_choices = ['Yes', 'No']

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'biography', 'birth_date', 'is_author']
        widgets = {
            'birth_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={'class': 'form-control', 'placeholder': 'Select your birthday', 'type': 'date'}),
            'is_author': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Would you like to be an author?'}),
            'biography': forms.Textarea(),
            } 
        
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'biography', 'birth_date', 'is_author']