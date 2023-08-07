from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    wallet_address = models.CharField(max_length=35, default=0x00000000000000000000000)

    def __str__(self):
        return self.user.username
    
