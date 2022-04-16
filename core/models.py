from http.client import CREATED
from msilib.schema import Class, File
from pickle import TRUE
from random import choices
from re import A
from unicodedata import name
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.forms import UUIDField
from matplotlib.pyplot import title
from numpy import true_divide 

AGE_CHOICES = (
  ('ALL', 'ALL'),
  ('Kids', 'Kids')
)
MOVIE_CHOICES = (
  ('seasonal','seasonal'),
  ('single','single')
)


class CustomUser(AbstractUser):
  profiles= models.ManyToManyField('Profile')
  
  
class Profile(models.Model):
  name= models.CharField(max_length=225)
  age_limit= models.CharField(max_length= 10, choices=AGE_CHOICES)
  uuid= models.UUIDField(default= uuid.uuid4)
  
class Movie(models.Model):
  title= models.CharField(max_length=225)
  description= models.TextField(blank=True, null=True)
  CREATED= models.DateTimeField(auto_now_add=True)
  uuid= models.UUIDField(default= uuid.uuid4)
  type= models.CharField(max_length=10, choices=MOVIE_CHOICES)
  videos= models.ManyToManyField('video')
  flyer = models.ImageField(upload_to= 'flyers')
  age_limit = models.CharField(max_length= 10, choices=AGE_CHOICES)

class Video(models.Model):
  title= models.CharField(max_length=225, blank=True, null=True)
  File= models.FileField(upload_to= 'movies')
  
  
