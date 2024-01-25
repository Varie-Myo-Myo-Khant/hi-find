from django.db import models
from user.models import User
from signup.models import lostUser

# Create your models here.
class Message(models.Model):
    sender = models.ForeignKey(lostUser, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(lostUser, on_delete=models.CASCADE, related_name='receiver')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
