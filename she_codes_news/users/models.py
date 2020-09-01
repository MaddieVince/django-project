from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    #Custom fields can be added here
    biography = models.CharField(max_length=200, blank=True)
    birth_date = models.DateTimeField()
    # bio_pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.username