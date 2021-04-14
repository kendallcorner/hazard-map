from django.db import models

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=60)
    latitude = models.CharField(max_length=60)
    longitude = models.CharField(max_length=60)
    zoom = models.IntegerField()

    def __str__(self):
        return self.name


class Scenario(models.Model):
    material = models.CharField(max_length=60)
    hidden = models.BooleanField(default=False)
    rangesHidden = models.BooleanField(default=False)
    name = models.CharField(max_length=60)
    scenarioId = models.CharField(max_length=60)
    latitude = models.CharField(max_length=60)
    longitude = models.CharField(max_length=60)
    range0 = models.CharField(max_length=60)
    frequency0 = models.CharField(max_length=60)
    range1 = models.CharField(max_length=60)
    frequency1 = models.CharField(max_length=60)
    range2 = models.CharField(max_length=60)
    frequency2 = models.CharField(max_length=60)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
