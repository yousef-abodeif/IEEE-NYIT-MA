from django.db import models
from colorfield.fields import ColorField
from django.utils import timezone
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)

    def publish(self):
        self.save()
    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField()
    desc = models.TextField()
    color = ColorField(default='#3498db')

    def publish(self):
        self.published_date = timezone.now()
        self.save()
    def __str__(self):
        return self.title

