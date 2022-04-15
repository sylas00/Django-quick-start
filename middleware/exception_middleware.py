from django.http import HttpResponseServerError, HttpResponse, JsonResponse
from django.utils.deprecation import MiddlewareMixin

from libs.exceptions import UserException


def handler_process(request, exception):
    """"""
    # todo logging
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
            # todo 用户操作异常日志
            return handler_process(request=request, exception=exception)
        if isinstance(exception, UserException):
            # todo 用户操作异常日志
            return handler_process(request=request, exception=exception)
        # 其他异常
        else:
            # 记录什么请求导致的异常
            # 怎么样同时知道异常发生的位置
            print(exception)
            return JsonResponse(data={"code": 10000, "errmsg": 12314})
