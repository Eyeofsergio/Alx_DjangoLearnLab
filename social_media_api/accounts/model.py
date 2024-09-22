from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField()
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics/')
    followers = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='following')

    def __str__(self):
        return self.username