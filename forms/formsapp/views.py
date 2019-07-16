from django.shortcuts import render
from formsapp.forms import FeedBackForm
def responseform(request):
     form = FeedBackForm()
     if request.method=='POST':
          form=forms.FeedBackForm(request.POST)
          if form.is_vallid():
              print("form vallidation success and print data")
              print('name:',form.cleaned_data[name])
              print('password',form.cleaned_data[password])
              print('rpassword',form.cleaned_data[rpassword])
              print('rollno:',form.cleaned_data[rollno])
              print('email:',form.cleaned_data[email])
              print('feedback:',form.cleaned_data[feedback])
              print('')
     return render(request, 'responeseform.html', {'form':form})
