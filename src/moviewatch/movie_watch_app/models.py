from django.db import models
from django.urls import reverse

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    year_released = models.PositiveIntegerField()
    watched = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('')

    def __str__(self):
        return self.title