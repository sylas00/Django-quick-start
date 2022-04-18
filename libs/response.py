from rest_framework import status
from rest_framework.response import Response

from libs.exception_enum import StatusCodeEnum

"""
基于DRF -- Response 的自定义响应
"""


class APIResponse(Response):
    def __init__(self, data: dict):
        """
        常用API响应
        :param data: 响应数据
        """
        data = {"code": StatusCodeEnum.SUCCESS.code, "msg": StatusCodeEnum.SUCCESS.msg, "data": data}
        super().__init__(status=status.HTTP_200_OK, data=data, )
