from .validator import Validator


class NationalCodeValidator(Validator):
    def validate(self, data):
        national_code = data.get('national_code')
        if national_code and len(national_code) != 10:
            return False, "National code must be 10 digits."
        return super().validate(data)
