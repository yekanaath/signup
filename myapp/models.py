from django.db import models

class usermodel(models.Model):
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    def __str__(self):
        return self.email
class house(models.Model):
    housename=models.CharField(max_length=50)
    phonenumber=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    cost=models.CharField(max_length=50)
    photo = models.ImageField(upload_to='house_photos/') 
    def __str__(self):
        return self.housename


      # Create your models here.
