from rest_framework import serializers
from insurance_policy.models.insurance_policy import InsurancePolicy
from person.models.person import Person
from insurance.models.insurance import Insurance
from insured.models.insured import Insured
from .person_serializer import PersonSerializer
from .insurance_serializer import InsuranceSerializer
from .insured_serializer import InsuredSerializer


class InsurancePolicySerializer(serializers.ModelSerializer):
    person = PersonSerializer()
    insurance = InsuranceSerializer()
    insured = InsuredSerializer()

    class Meta:
        model = InsurancePolicy
        fields = ['person', 'insurance', 'insured', 'start_date',
                  'end_date', 'unique_id', 'confirmed_at']

    def create(self, validated_data):
        person_data = validated_data.pop('person')
        insurance_data = validated_data.pop('insurance')
        insured_data = validated_data.pop('insured')

        person, _ = Person.objects.get_or_create(**person_data)
        insurance, _ = Insurance.objects.get_or_create(**insurance_data)
        insured, _ = Insured.objects.get_or_create(**insured_data)

        insurance_policy = InsurancePolicy.objects.create(
            person=person,
            insurance=insurance,
            insured=insured,
            **validated_data
        )
        return insurance_policy
