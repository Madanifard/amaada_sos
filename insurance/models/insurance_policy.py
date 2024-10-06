from django.db import models
from .person import Person
from .insurance import Insurance
from .insured import Insured

class InsurancePolicy(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    insurance = models.ForeignKey(Insurance, on_delete=models.CASCADE)
    insured = models.ForeignKey(Insured, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    unique_id = models.CharField(max_length=50, unique=True)
    confirmed_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)