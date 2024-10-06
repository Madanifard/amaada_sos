import re
from .validator import Validator


class EmailValidator(Validator):
    def validate(self, data):
        email = data.get('email')
        if email and not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return False, "Invalid email format."
        return super().validate(data)
