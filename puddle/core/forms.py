from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your username',
            'class': 'h-8 w-full rounded-md border border-slate-300 text-sm pl-2 bg-transparent outline-blue-600 shadow-sm',
            
        }))   
    password = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': '********',
            'class': ' h-8 w-full rounded-md border border-slate-300 text-sm pl-2 bg-transparent outline-blue-600 shadow-sm',
            
        }))
class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


    username = forms.CharField(widget=forms.TextInput(attrs={
            'placeholder': 'Your first name',
            'class': 'h-8 w-full rounded-md border border-slate-300 text-sm pl-2 bg-transparent outline-blue-600 shadow-sm',
            
        }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
            'placeholder': 'Your email',
            'class': 'h-8 w-full rounded-md border border-slate-300 text-sm pl-2 bg-transparent outline-blue-600 shadow-sm',
            
        }))    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': '********',
            'class': 'h-8 w-full rounded-md border border-slate-300 text-sm pl-2 bg-transparent outline-blue-600 shadow-sm',
            
        }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'placeholder': '********',
            'class': 'h-8 w-full rounded-md border border-slate-300 text-sm pl-2 bg-transparent outline-blue-600 shadow-sm',
            
        }))                       
