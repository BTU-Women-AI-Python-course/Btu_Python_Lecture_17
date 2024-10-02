from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Blogs(models.Model):
    title = models.CharField(max_length=255)
    context = models.TextField()

    author = models.ForeignKey(User, on_delete=models.CASCADE)
