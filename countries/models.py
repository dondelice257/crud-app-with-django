from django.db import models

# Create your models here.

class Country(models.Model):
    name=models.CharField(max_length=255)
    capital=models.CharField(max_length=255)
    people=models.IntegerField(null=True)
    area=models.IntegerField(null=True)
    

    