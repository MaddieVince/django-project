from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    #Custom fields can be added here
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    biography = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField()
    is_author = models.BooleanField()
    # bio_pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username