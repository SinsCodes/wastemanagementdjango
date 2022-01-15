from django.db import models

# Create your models here.

class Admin_Reg(models.Model):
    Admin_name = models.CharField(max_length=100)
    Age = models.IntegerField()
    Email = models.EmailField(max_length=100)
    Phone = models.CharField(max_length=100)
    Username = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)

class Rest_Reg(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    images = models.CharField(max_length=200, default='null')
    info = models.CharField(max_length=200, default='null')


class Ngo_Reg(models.Model):

    name = models.CharField(max_length=100)
    institution_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    postcode = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    images = models.CharField(max_length=200, default='null')
    info = models.CharField(max_length=200, default='null')



class Employee(models.Model):

    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
