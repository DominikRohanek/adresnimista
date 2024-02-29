from django.db import models
from django.contrib.auth.models import User

class Place(models.Model):
    identifier = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.identifier

class City(models.Model):
    name = models.CharField(max_length=40)
    postalcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.postalcode})" 

class Address(models.Model):

    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    street = models.CharField(max_length=50)
    orientation_number = models.CharField(max_length=10)
    descriptive_number = models.CharField(max_length=10)
    registration_number = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.street} ({self.orientation_number})" 


        