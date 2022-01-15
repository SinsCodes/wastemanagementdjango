from django import forms
from django.forms import ModelForm
from .models import Rest_Reg

class RestForm(forms.Form):
    username = forms.CharField(label='user name',max_length=100)
    password = forms.CharField(label='password')






class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)



