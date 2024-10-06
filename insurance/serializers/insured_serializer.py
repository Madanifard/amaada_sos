from rest_framework import serializers
from insurance.models.insured import Insured

class InsuredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insured
        fields = ['name', 'unique_id']
