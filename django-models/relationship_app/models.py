from django.db import models
from django.contrib.auth.models import User 
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserProfile(models.Model):
    ROLE_CHOICE = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )
    user = models.OneToOneField(User, on_delte=model.CASCADE)
    role = models.CharField (max_length=20, choices=ROLE_CHIOCES)

receiver(post_save, sender=User)
def create_user_profile(sender, instance,created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

receiver(post_save, sender=User)
def save_user_profile(sender, instance,created, **kwargs):
    instance.userprofile.save()
# Model Creations        
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    class Meta:
        permissions = (
            ('can_add_book', 'Can add book'),
            (can_change_book', 'Can change book')
            ('can_delete_book', 'Can delete book')
        )
    
    def __str__(self):
        return self.title

class Library(models.Model):
        return self.name

    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return self.name

class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
