from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Share(models.Model):
    body = models.TextField(null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[0:50]

class Stock(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name