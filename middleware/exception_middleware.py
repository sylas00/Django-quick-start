import logging

from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from libs.exception_enum import StatusCodeEnum

from libs.exceptions import UserException
import traceback

logger = logging.getLogger('django')


def handler_process(request, exception):
    """"""
    return JsonResponse(data={"code": exception.code, "errmsg": exception.errmsg})


class ExceptionMiddleware(MiddlewareMixin):
    """统一异常处理中间件"""

    def process_exception(self, request, exception):
        """
        统一异常处理
        :param request: 请求对象
        :param exception: 异常对象
        :return:
        """
        # 异常处理
        if isinstance(exception, UserException):
            return handler_process(request=request, exception=exception)
        if isinstance(exception, UserException):
            return handler_process(request=request, exception=exception)
        # 其他异常
        else:
            logger.error(traceback.format_exc())
            return JsonResponse(data={"code": StatusCodeEnum.SERVER_ERR.code, "errmsg": StatusCodeEnum.SERVER_ERR.msg})
