from django.db import models
from django import forms

CHOICES = [("tourist","tourist"),
          ("salesman","salesman"),
          ("admin","admin") ]

class User(models.Model):
    username = models.CharField(max_length=50,unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    identity = models.CharField(max_length=15,default="tourist")

    class Meta:
        db_table = "user"
    
class RegisterForm(forms.ModelForm):
    password = forms.CharField(max_length=128,widget = forms.PasswordInput)
    password2 = forms.CharField(max_length=128,widget = forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ("username", "email", "password")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password =forms.CharField(max_length=128,widget = forms.PasswordInput)
    identity = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())
    
