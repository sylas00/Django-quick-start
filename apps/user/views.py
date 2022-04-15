from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# Create your views here.
from libs.exception_enum import StatusCodeEnum
from libs.exceptions import UserException


class UserRegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, req):
        if not req.data.get("username"):
            raise UserException(StatusCodeEnum.USERNAME_EXIST)
        return Response(status=status.HTTP_200_OK, data={"create": "成功"})
