from drf_spectacular.utils import extend_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers.full_data_serializer import FullDataSerializer


class FullDataAPIView(APIView):

    permission_classes = [AllowAny]

    @extend_schema(
        summary="Create Full Data",
        description="This API allows the user to send a large JSON with nested data for plan, person, insurance policy, etc., and stores the validated data in the database.",
        request=FullDataSerializer,
        responses={201: dict, 400: dict},
    )
    def post(self, request):
        serializer = FullDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data successfully saved"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
