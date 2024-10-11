from rest_framework import serializers
from insurance.models.insurance import Insurance


class InsuranceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['name', 'unique_id']

    def validate_unique_id(self, value):
        try:
            insurance = Insurance.objects.get(unique_id=value)
            return insurance.unique_id
        except Insurance.DoesNotExist:
            return value

    def create(self, validated_data):
        insurance, created = Insurance.objects.get_or_create(
            unique_id=validated_data.get('unique_id'),
            defaults={'name': validated_data.get('name')}
        )
        return insurance
