from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Letter
from . import serializers


class Letters(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="쪽지 조회 api",
        responses={
            200: openapi.Response(
                description="Successful Response",
                schema=serializers.LetterSerializer(),
            )
        },
    )
    def get(self, request):
        letter = Letter.objects.filter(sender=request.user)
        serializer = serializers.LetterSerializer(letter)
        return Response(serializer.data)
    
    def post(self,request):
        letter = Letter.objects.filter(sender=request.user)
        serializer = serializers.LetterSerializer(data=request.data)
        #미완성
