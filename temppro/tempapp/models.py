from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=20)
    fee=models.IntegerField()
    emial=models.EmailField()
    obj=models.Manager()
    def __str__(self):
        return self.emial
    class meta:
        varbose_emial=("emial",)
class mointer(models.Model):
    student=models.OneToOneField(student,on_delete=models.CASCADE,)
    mname=models.CharField(max_length=20)
 