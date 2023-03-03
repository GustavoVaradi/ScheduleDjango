from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class Contacs(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=20)
    mail = models.CharField(max_length=100)
    creation_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)