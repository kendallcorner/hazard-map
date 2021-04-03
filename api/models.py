from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=60)
    latitude = models.CharField(max_length=60)
    longitude = models.CharField(max_length=60)
    zoom = models.IntegerField()

    def __str__(self):
        return self.name

