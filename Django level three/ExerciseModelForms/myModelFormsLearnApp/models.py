from django.db import models

# Create your models here.


class SignUp(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField()
