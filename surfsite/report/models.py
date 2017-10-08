from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Beach(models.Model):
    name = models.CharField(max_length=50)
    high = models.SmallIntegerField()
    low = models.SmallIntegerField()
    wind = models.SmallIntegerField()
    tide = models.DecimalField(max_digits=3, decimal_places=2)

    def __str__(self):
        return self.name
