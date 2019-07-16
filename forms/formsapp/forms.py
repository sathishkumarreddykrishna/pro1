from django import forms
from django.core import validators

class FeedBackForm(forms.Form):
  name=forms.CharField()
  password=forms.CharField()
  rpassword=forms.CharField(label='Re Enter password',widget=forms.PasswordInput)
  rollno=forms.CharField()
  email=forms.EmailField()
  feedback=forms.CharField()
  bot_hander=forms.CharField(required=False,widget=forms.HiddenInput)

  def clean(self):
    print("vallidating password match")
    total_cleaned_data=clean()
    fpwrd=total_cleaned_data['password']
    spwd=total_cleaned_data['rpassword']
    if fpwrd!=spwd:
      raise forms.VallisationError("both password must be matched")
    bot_hander_value=total_cleaned_data['bot_hander']
    if len(bot_hander_value)>0:
        raise forms.VallidationsError('request from Bot --con,t subtions')
