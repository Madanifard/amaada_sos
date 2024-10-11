from rest_framework import serializers
from plan.models.plan import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['name', 'unique_id']

    def validate_unique_id(self, value):

        try:
            plan = Plan.objects.get(unique_id=value)
            return plan.unique_id
        except Plan.DoesNotExist:
            return value

    def create(self, validated_data):
        plan, created = Plan.objects.get_or_create(
            unique_id=validated_data.get('unique_id'),
            defaults={'name': validated_data.get('name')}
        )
        return plan
