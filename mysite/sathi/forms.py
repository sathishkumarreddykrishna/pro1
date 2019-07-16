from django import forms
from models import Home

class login_form(forms.Form):
    first_name=forms.CharField(max_length=30,blank=True)
    last_name=forms.CharField(max_length=30,blank=True)
    mobile_number=forms.IntegerField(blank=True,primary_key=True)
    adders=forms.TextField(max_length=300)
    password=forms.CharField(max_length=10)
    
