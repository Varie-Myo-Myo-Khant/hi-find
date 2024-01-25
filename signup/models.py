from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class lostUser(AbstractUser):

    username = models.CharField(max_length=30,unique=True)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=128)  # Store hashed passwords securely
    gender = models.CharField(max_length=10, choices=[('M', 'Male'), ('F', 'Female')],default='M')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username