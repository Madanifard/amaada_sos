from django.db import models


class Insurance(models.Model):
    name = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
