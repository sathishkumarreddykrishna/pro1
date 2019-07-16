from django.db import models
# Create your models here.
class Home(models.Model):
    first_name=models.CharField(max_length=30,blank=True)
    last_name=models.CharField(max_length=30,blank=True)
    mobile_number=models.IntegerField(blank=True,primary_key=True)
    adders=models.TextField(max_length=300)
    password=models.CharField(max_length=10)
 
   



