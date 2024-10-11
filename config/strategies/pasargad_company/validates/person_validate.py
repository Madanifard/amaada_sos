import re


class PersonValidate:
    required_fields = ['first_name', 'last_name', 'email', 'mobile_number',
                       'national_code', 'birth_date']

    def validate(self, data):
        """
        Validate the input data to ensure required fields exist.
        :param data: Dictionary containing the data to validate.
        :return: Tuple of (is_valid, errors), where is_valid is a boolean, and errors is a list of missing fields.
        """
        errors = []
        for field in self.required_fields:
            if field not in data or data[field] is None:
                errors.append(f"Missing required field: {field}")

            if field == 'email':
                if not re.match(r'[^@]+@[^@]+\.[^@]+', data[field]):
                    errors.append(f"Email Format Is Invalid")

            if field == 'mobile':
                if not re.match(r'^\+?[1-9]\d{1,14}$', data[field]):
                    errors.append(f"Mobile Format Is Invalid")

        return len(errors) == 0, errors

    def format_data(self, data):
        """
        Format the data (e.g., converting first_name to lowercase).
        :param data: Dictionary containing the data to format.
        :return: Formatted data.
        """
        formatted_data = data.copy()

        # Convert 'name' field to lowercase if it exists
        if 'first_name' in formatted_data:
            formatted_data['first_name'] = formatted_data['first_name'].lower()

        if 'last_name' in formatted_data:
            formatted_data['last_name'] = formatted_data['last_name'].lower()

        # Add other formatting rules as needed
        # For example, we could trim whitespace or convert dates here

        return formatted_data
