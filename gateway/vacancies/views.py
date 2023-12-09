from rest_framework.request import Request
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView



class Hello(APIView):
    permission_classes = (permissions.AllowAny,)

    @swagger_auto_schema(operation_id='get-hello', )
    def get(self, request: Request):
        return Response(data=f"hello, Django", status=status.HTTP_200_OK)
