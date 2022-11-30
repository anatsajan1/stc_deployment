from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Users(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    phone=models.IntegerField()
    password=models.CharField(max_length=100)  

class Application(models.Model):
    username=models.CharField(max_length=100)
    gender=models.CharField(max_length=32)
    email=models.EmailField(max_length=100)
    income=models.IntegerField()
    occupation=models.IntegerField()
    category=models.IntegerField()
    place=models.CharField(max_length=100)
    institute=models.CharField(max_length=100)
    source=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)