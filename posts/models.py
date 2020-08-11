from django.db import models

# Create your models here.

class User(models.Model):
    email       = models.EmailField
    password    = models.CharField(max_length=25)
    
    first_name  = models.CharField(max_length=25)
    last_name   = models.CharField(max_length=25)

    bio         = models.TextField()

    birthday    = models.DateField()
    created     = models.DateTimeField()         
    modified    = models.DateTimeField()
