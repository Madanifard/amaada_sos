from rest_framework import serializers
from insurance.models.insurance import Insurance


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['name', 'unique_id']
