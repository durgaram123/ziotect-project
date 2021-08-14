from django.db import models
from django.contrib.auth.models import User

class Details(models.Model):
    title = models.CharField(max_length=255,null=True)
    phone_number = models.CharField(max_length=255,null=True)
    field_name = models.EmailField(max_length=355,null=True)
    body = models.TextField(null=True)

def __str__(self):
    return  self.title


class News(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    title = models.CharField(max_length=255,null=True)
    body = models.TextField(null=True)

 

class Subscribe(models.Model):
    email = models.EmailField(max_length=255,null=True)

def __str__(self):
    return  self.email

class Testimonial(models.Model):
    image = models.ImageField(upload_to='images/',null=True)
    title = models.CharField(max_length=255,null=True)
    text = models.TextField(max_length=255,null=True)
    body = models.TextField(null=True)

    image1 = models.ImageField(upload_to='images/',null=True)
    title1 = models.CharField(max_length=255,null=True)
    text1 = models.TextField(max_length=255,null=True)
    body1 = models.TextField(null=True)

    image2 = models.ImageField(upload_to='images/',null=True)
    title2 = models.CharField(max_length=255,null=True)
    text2 = models.TextField(max_length=255,null=True)
    body2 = models.TextField(null=True)

def __str__(self):
    return  self.title 

class Top(models.Model):
    title = models.CharField(max_length=255,null=True)
    body = models.TextField(null=True)
    

    title1 = models.CharField(max_length=255,null=True)
    body1 = models.TextField(null=True)
    

    title2 = models.CharField(max_length=255,null=True)
    body2 = models.TextField(null=True)

    image = models.ImageField(upload_to='images/',null=True)

    
    






    
