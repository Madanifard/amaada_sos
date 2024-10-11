from rest_framework import serializers
from person.models.person import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'mobile_number',
                  'national_code', 'birth_date', 'father_name', 'place_of_issue',
                  'created_at', 'updated_at']

    def get_or_create(self, validated_data):
        national_code = validated_data.get('national_code')
        person, created = Person.objects.get_or_create(
            national_code=national_code,
            defaults={
                'first_name': validated_data.get('first_name'),
                'last_name': validated_data.get('last_name'),
                'email': validated_data.get('email'),
                'mobile_number': validated_data.get('mobile_number'),
                'birth_date': validated_data.get('birth_date'),
                'father_name': validated_data.get('father_name', ''),
                'place_of_issue': validated_data.get('place_of_issue'),
            }
        )

        return person
