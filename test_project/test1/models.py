from django.db import models

# Create your models here.
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    place = models.CharField(max_length=255)

    def __str__(self):
        return self.name