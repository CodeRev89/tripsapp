from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

class Profile(models.Model): 
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    image_field=models.ImageField()
    bio_field=models.CharField(max_length=500)    
