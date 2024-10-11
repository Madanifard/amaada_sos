from django.db import models


class Insured(models.Model):
    name = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
