from django.db import models
from django.contrib.auth.models import User
from django.db.models import aggregates
from django.db.models import fields
from django.db.models.fields import EmailField
from django import forms
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.modelfields import PhoneNumberField

class Customer(User):
    age=models.IntegerField()
    address=models.TextField(max_length=300)
    contact=models.CharField(max_length=15)
    phone=PhoneNumberField()
    
    def __str__(self):
        return self.username

class BookTable(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    phone=PhoneNumberField()
    bdate=models.DateField()
    btime=models.TimeField()
    npeople=models.IntegerField()
    bmessage=models.TextField(max_length=300)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = PhoneNumberField(blank=True)
    subject = models.CharField(max_length=300)
    message = models.TextField(max_length=1000)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
'''------------------Forms section------------------------------'''

class Customer1Form(UserCreationForm):
    class Meta:
        model=Customer
        fields=['first_name','last_name','email','contact','address','age','username']

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model=ContactMessage
        fields=['name','email','phone','subject','message']