from django.db import models
from django.urls import reverse, reverse_lazy


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=60)
    info = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("home")
