from django.db import models
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your models here.
class CustomUser (AbstractUser):
    block = models.BooleanField(name='block', default=False)
    created_at = models.DateTimeField(name="created_at", auto_now=True)
    phone = models.CharField(name="phone", max_length=30, blank=False, unique=True)
    email = models.CharField(name="email", max_length=30, blank=False, unique=True)
    image = models.ImageField(name="image", upload_to="images/",  default="images/user.png", blank=False)
    
    def __str__ (self) -> str:
        return self.phone

    def get_absolute_url (self):
        return reverse('login')