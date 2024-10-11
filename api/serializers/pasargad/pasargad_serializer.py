from rest_framework import serializers
from api.serializers.base.plan_serializer import PlanSerializer
from api.serializers.base.insurance_policy_serializer import InsurancePolicySerializer
from config.strategies.context import StrategyContext


class PasargadPlanSerializer(PlanSerializer):

    class Meta(PlanSerializer.Meta):
        fields = PlanSerializer.Meta.fields

    def validate(self, data):

        context = StrategyContext(self.context['company_name'])
        is_valid, errors, formatted_data = context.process('plan', data)

        if is_valid is False:
            return serializers.ValidationError(errors)
        else:
            return formatted_data


class PasargadInsurancePolicySerializer(InsurancePolicySerializer):

    class Meta(InsurancePolicySerializer.Meta):
        fields = InsurancePolicySerializer.Meta.fields

    def validate(self, data):

        formatted_data = {
            'person': {},
            'insurance': {},
            'insured': {},
            'start_date': None,
            'end_date': None,
            'unique_id': None,
            'confirmed_at': None
        }
        errors_list = []

        context = StrategyContext(self.context['company_name'])
        is_valid_person, errors_person, formatted_data_person = context.process(
            'person',
            data['person'])

        if is_valid_person:
            formatted_data['person'].update(formatted_data_person)
        else:
            errors_list.append(errors_person)

        is_valid_insurance, errors_insurance, formatted_data_insurance = context.process(
            'insurance',
            data['insurance'])

        if is_valid_insurance:
            formatted_data['insurance'].update(formatted_data_insurance)
        else:
            errors_list.append(errors_insurance)

        is_valid_insured, errors_insured, formatted_data_insured = context.process(
            'insured',
            data['insured'])
        
        if is_valid_insured:
            formatted_data['insured'].update(formatted_data_insured)
        else:
            errors_list.append(errors_insured)

        # this for insurance Policy
        formatted_data['start_date'] = data['start_date']
        formatted_data['end_date'] = data['end_date']
        formatted_data['unique_id'] = data['unique_id']
        formatted_data['confirmed_at'] = data['confirmed_at']

        if errors_list:
            raise serializers.ValidationError(errors_person)
        else:
            return formatted_data


class PasargadSerializer(serializers.Serializer):
    plan = PasargadPlanSerializer()
    insurance_policy = PasargadInsurancePolicySerializer()

    def create(self, validated_data):
        plan_data = validated_data.pop('plan')
        insurance_policy_data = validated_data.pop('insurance_policy')

        plan_serializer = PasargadPlanSerializer(data=plan_data)
        plan_serializer.context['company_name'] = 'pasargad'
        plan_serializer.is_valid(raise_exception=True)
        plan_serializer.save()

        insurance_policy_serializer = PasargadInsurancePolicySerializer(
            data=insurance_policy_data)
        insurance_policy_serializer.context['company_name'] = 'pasargad'
        insurance_policy_serializer.is_valid(raise_exception=True)
        insurance_policy_serializer.save()

        return validated_data
