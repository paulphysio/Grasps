from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import CharField, ModelForm, TextInput, EmailInput, ValidationError, EmailField, PasswordInput, Textarea
from .models import contact

class UserRegistrationForm(UserCreationForm):
    email = EmailField()

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        widgets = {
            'username': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Username'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Email'
            }),
            'password1': PasswordInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'password'
            }),
            'password2': PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': 'confirm password'
            })
        }

class contact_form(ModelForm):
    
    class Meta:
        model = contact

        fields = [
            'name',
            'email',
            'subject',
            'message',
        ]
        widgets = {
            'name': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Email'
            }),
            'subject': TextInput(attrs={
                'class':"form-control",
                'style': 'max-width: 300px',
                'placeholder': 'Subject'
            }),
            'message': Textarea(attrs={
                'class': "form-control",
                'style': 'max-width: 300px',
                'rows': '5',
                'placeholder': 'Message',
                
            })
        }

