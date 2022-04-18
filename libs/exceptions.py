"""
自定义异常
"""


class RootException(Exception):
    """预留拓展用"""
    pass


class CommonException(RootException):
    """通用异常类"""

    def __init__(self, enum_cls):
        self.code = enum_cls.code
        self.errmsg = enum_cls.msg
        super().__init__()


class UserException(CommonException):
    """用户异常"""
    pass


class BusinessException(CommonException):
    """业务异常类"""
    pass


class DatabaseException(CommonException):
    """数据库异常类"""
    pass
