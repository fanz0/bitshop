from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    wallet_address = models.TextField(blank=True)
    private_key = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
    
