from django.db import models

class student(models.Model):
    name =models.CharField(max_length=10)
    fee =models.IntegerField( )
    email =models.EmailField( )

    def __str__(self):
        return self.name

class deteils(models.Model):
    student=models.ForeignKey(student,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=10)