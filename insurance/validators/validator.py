class Validator:
    def __init__(self, next_validator=None):
        self.next_validator = next_validator

    def validate(self, data):
        if self.next_validator:
            return self.next_validator.validate(data)
        return True, None
