from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=40)
    postalcode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.name} ({self.postalcode})" 
        
    class Meta:
        unique_together=["name","postalcode"]





class Address(models.Model):

    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    street = models.CharField(max_length=50)
    orientation_number = models.CharField(max_length=10)
    descriptive_number = models.CharField(max_length=10)

    def __str__(self):
        if self.street:
            if self.orientation_number:
                return f"{self.street} {self.descriptive_number}/{self.orientation_number}"
            return f"{self.street} {self.descriptive_number}" 
        return f"{self.city.name} {self.descriptive_number}"

    class Meta:
        ordering=["street","orientation_number","descriptive_number"]