from os import name
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=256)
    principal = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def get_absolute_url(self):
        return reverse("BasicApp:detail", kwargs={'pk': self.pk})


class Student(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name='students')
