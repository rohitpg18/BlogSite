from django.db import models
from django.contrib.auth.models import User
import uuid

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=13 , default=None)
    otp = models.CharField(max_length=100 , default=None , null=True, blank=True)
    uid = models.UUIDField(default=uuid.uuid4)

    def __str__(self):
        return self.user.username


