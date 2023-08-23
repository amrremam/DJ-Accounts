from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to='''image_upload_path''')
    
    def __str__(self):
        return str(self.user)