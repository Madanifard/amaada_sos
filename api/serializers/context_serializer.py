from api.serializers.pasargad.pasargad_serializer import PasargadSerializer


class ContextSerializer:
    def __init__(self, company_name):
        self.serializer_class = self.get_serializer_class(company_name)
        self.serializer_instance = None

    def get_serializer_class(self, company_name):
        if company_name == 'pasargad':
            return PasargadSerializer
        else:
            raise ValueError("Unknown insurance company")

    def get_serializer(self, data):
        self.serializer_instance = self.serializer_class(data=data)
        return self.serializer_instance

    def is_valid(self):
        if self.serializer_instance is None:
            raise ValueError(
                "Serializer is not initialized with data. Call `get_serializer` first.")
        return self.serializer_instance.is_valid(raise_exception=True)

    def save(self):
        if self.serializer_instance is None:
            raise ValueError(
                "Serializer is not initialized with data. Call `get_serializer` first.")
        return self.serializer_instance.save()

    def data(self):
        if self.serializer_instance is None:
            raise ValueError(
                "Serializer is not initialized with data. Call `get_serializer` first.")
        return self.serializer_instance.data

    def errors(self):
        if self.serializer_instance is None:
            raise ValueError(
                "Serializer is not initialized with data. Call `get_serializer` first.")
        return self.serializer_instance.errors
