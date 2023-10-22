from django.db import models

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=200)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class DroupOuts(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    