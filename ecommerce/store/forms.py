from django import forms
from django.forms import ModelForm
from .models import Customer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('user', 'name', 'email')


