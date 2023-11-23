from django.db import models

# Create your models here.

class Transaction_model(models.Model):
    name = models.CharField(max_length=48)
    description = models.TextField()
    is_successful = models.BooleanField(default=False)