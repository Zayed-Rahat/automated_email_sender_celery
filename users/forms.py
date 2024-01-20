from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

from django.contrib.auth.models import User
from django import forms
 

 
class UserForm(UserCreationForm):
    '''
    Form that uses built-in UserCreationForm to handle user creation
    '''

    username = forms.CharField(max_length=50, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Username..'}))
    email = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={
            'placeholder': '*Email..'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '*Password..',}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': '*Confirm Password..',}))
    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2', )
 
 
 
 
class AuthForm(AuthenticationForm):
    '''
    Form that uses built-in AuthenticationForm to handle user auth
    '''
    email = forms.EmailField(max_length=254, required=True,
        widget=forms.TextInput(attrs={'placeholder': '*Email..',}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': '*Password..',}))
 
    class Meta:
        model = User
        fields = ('email','password', )
 