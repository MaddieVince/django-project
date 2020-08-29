from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    #Custom fields can be added here
    pass

    def __str__(self):
        return self.username
