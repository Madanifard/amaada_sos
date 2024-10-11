from django.db import models
from django.core.exceptions import ObjectDoesNotExist


class Insurance(models.Model):
    name = models.CharField(max_length=100)
    unique_id = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def find_by_unique_id(cls, unique_id):
        try:
            return cls.objects.get(unique_id=unique_id)
        except ObjectDoesNotExist:
            return None
