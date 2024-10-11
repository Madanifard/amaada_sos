from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers.context_serializer import ContextSerializer
from insurance.models.insurance import Insurance


class InsuranceAPIView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        company_unique_id = request.data['insurance_policy']['insurance']['unique_id']
        insurance = Insurance.find_by_unique_id(company_unique_id)
        if insurance:
            context_serializer = ContextSerializer(company_name=insurance.name)
            serializer = context_serializer.get_serializer(request.data)
            serializer.context['company_name'] = insurance.name

            if context_serializer.is_valid():
                context_serializer.save()
                return Response({"message": "Data successfully saved"},
                                status=status.HTTP_201_CREATED)
            else:
                return Response(context_serializer.errors,
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Insurance Info Invalid'})
