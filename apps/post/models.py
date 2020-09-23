from django.db import models
from colorfield.fields import ColorField
from apps.user.models import Profile
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=10)
    color = ColorField(default='#000000')

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=128)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField(upload_to='images/')
    exposee = models.CharField(max_length=512)
    text = HTMLField()
    publish_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title