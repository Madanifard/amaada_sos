from rest_framework import serializers
from plan.models.plan import Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ['name', 'unique_id']

    def validate(self, data):
        return data
