from django.db import models
from django.contrib.auth.models import AbstractUser
class Place(models.Model):
    Name=models.CharField(max_length=30)
    Desc=models.CharField(max_length=100)
    Cover=models.ImageField(upload_to='app1/img', null=True, blank=True)


class Team(models.Model):
    Name=models.CharField(max_length=30)
    Desc=models.CharField(max_length=100)
    Img=models.ImageField(upload_to='app1/images', null=True, blank=True)

class Myuser(AbstractUser):
    place = models.CharField(max_length=30)
    phone = models.CharField(max_length=30)


