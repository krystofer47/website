from django.db import models
from django.contrib.auth.models import User

from . import signals

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    favourite_color = models.CharField(
        max_length=3,
        choices = [
            ('red', 'Red'),
            ('blu', 'Blue'),
            ('gre', 'Green')
        ],
        default="unknown"
    )
    modified = models.DateTimeField('last edited', auto_now=True)

    def __str__(self):
        return self.user.username
    
    def __eq__(self):
        return self.user.username