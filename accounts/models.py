from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=30, null=True, blank=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    image = models.ImageField(upload_to='''image_upload_path''',null=True, blank=True)
    
    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created, **kwargs):
    if created:
        profile.objects.create(
            user = instance
        )