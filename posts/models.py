from django.db import models
from signup.models import lostUser
# Create your models here.

class lostItems(models.Model):
    post_id = models.AutoField(primary_key=True,unique=True)
    status = models.CharField(max_length=10, default='active' )
    user = models.ForeignKey(lostUser, on_delete=models.CASCADE)
    
    postTitle = models.CharField(max_length=200)
    lostItem = models.CharField(max_length=150)
    location = models.CharField(max_length=150)
    description = models.CharField(max_length=1500)
    fileUpload = models.FileField(upload_to='uploads/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.postTitle

   
