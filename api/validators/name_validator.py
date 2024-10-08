from .validator import Validator


class NameValidator(Validator):
    def normalize_name(self, name):
        return name.strip().title()

    def validate(self, data):
        if 'first_name' in data:
            data['first_name'] = self.normalize_name(data['first_name'])
        if 'last_name' in data:
            data['last_name'] = self.normalize_name(data['last_name'])
        return super().validate(data)
