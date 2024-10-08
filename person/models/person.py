from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=20)
    national_code = models.CharField(max_length=10, unique=True)
    birth_date = models.DateField()
    father_name = models.CharField(max_length=100, blank=True)
    place_of_issue = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
