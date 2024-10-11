class PlanValidate:
    required_fields = ['name', 'unique_id']

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

        return len(errors) == 0, errors

    def format_data(self, data):
        """
        Format the data (e.g., converting names to lowercase).
        :param data: Dictionary containing the data to format.
        :return: Formatted data.
        """
        formatted_data = data.copy()

        # Convert 'name' field to lowercase if it exists
        if 'name' in formatted_data:
            formatted_data['name'] = formatted_data['name'].lower()

        # Add other formatting rules as needed
        # For example, we could trim whitespace or convert dates here

        return formatted_data
