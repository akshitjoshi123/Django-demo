from django.db import models

# Create your models here.

class userInfo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password1 = models.CharField(max_length=30)
