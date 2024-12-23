from django.db import models
from test1.models import *

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=255)
    o_id =models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="employees")