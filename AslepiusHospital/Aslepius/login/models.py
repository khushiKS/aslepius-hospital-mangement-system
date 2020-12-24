from django.db import models
from django.contrib.auth.models import User



class Register(models.Model):
    patientid= models.AutoField(primary_key=True,)
    '''name = models.CharField(max_length=50)'''
    dob = models.DateField()
    gender = models.CharField(max_length=1)
    email = models.ForeignKey(User, on_delete= models.CASCADE,)
    '''email = models.EmailField()'''
    '''passwd = models.CharField(max_length=15)'''
    '''confirmpasswd = models.CharField(max_length=15)'''
    mobile = models.BigIntegerField()
    Add1 = models.CharField(max_length=70)
    Add2 = models.CharField(max_length=65)
    Add3 = models.CharField(max_length=65)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()


class Temporary_passwd(models.Model):
    email= models.EmailField(primary_key=True,)
    temppasswd= models.CharField(max_length=8)


class Forgot_Password(models.Model):
    email = models.EmailField(primary_key = True)
    otp = models.BigIntegerField()
# Create your models here.
