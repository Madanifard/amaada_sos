from rest_framework import serializers
from .plan_serializer import PlanSerializer
from .insurance_policy_serializer import InsurancePolicySerializer


class FullDataSerializer(serializers.Serializer):
    plan = PlanSerializer()
    insurance_policy = InsurancePolicySerializer()

    def validate(self, data):
        plan_data = data.get('plan')
        insurance_policy_data = data.get('insurance_policy')

        if not plan_data:
            raise serializers.ValidationError("Plan data is required.")

        if not insurance_policy_data:
            raise serializers.ValidationError(
                "Insurance Policy data is required.")

        PlanSerializer(data=plan_data).is_valid(raise_exception=True)
        InsurancePolicySerializer(
            data=insurance_policy_data).is_valid(raise_exception=True)

        return data

    def create(self, validated_data):

        plan_data = validated_data.pop('plan')
        insurance_policy_data = validated_data.pop('insurance_policy')

        plan_serializer = PlanSerializer(data=plan_data)
        plan_serializer.is_valid(raise_exception=True)
        plan_serializer.save()

        insurance_policy_serializer = InsurancePolicySerializer(
            data=insurance_policy_data)
        insurance_policy_serializer.is_valid(raise_exception=True)
        insurance_policy_serializer.save()

        return validated_data
