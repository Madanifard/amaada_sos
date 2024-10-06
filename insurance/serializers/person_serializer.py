from rest_framework import serializers
from insurance.models.person import Person
from insurance.validators.email_validator import EmailValidator
from insurance.validators.national_code_validator import NationalCodeValidator
from insurance.validators.name_validator import NameValidator


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'mobile_number',
                  'national_code', 'birth_date', 'father_name', 'place_of_issue']

    def validate(self, data):
        # create Chain of Validation
        validator_chain = NameValidator(
            next_validator=EmailValidator(
                next_validator=NationalCodeValidator()
            )
        )
        # run Validation
        is_valid, error = validator_chain.validate(data)
        if not is_valid:
            raise serializers.ValidationError(error)

        return data
