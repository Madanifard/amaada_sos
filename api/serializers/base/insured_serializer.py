from rest_framework import serializers
from insured.models.insured import Insured

class InsuredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insured
        fields = ['name', 'unique_id']

    def validate_unique_id(self, value):

        try:
            insured = Insured.objects.get(unique_id=value)
            return insured.unique_id
        except Insured.DoesNotExist:
            return value

    def create(self, validated_data):
        insured, created = Insured.objects.get_or_create(
            unique_id=validated_data.get('unique_id'),
            defaults={'name': validated_data.get('name')}
        )
        return insured
