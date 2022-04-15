from enum import Enum


class StatusCodeEnum(Enum):
    """状态码枚举类"""

    SUCCESS = (0, '成功')
    ERROR = (-1, '错误')
    SERVER_ERR = (500, '服务器异常')

    USERNAME_EXIST = (5001, '用户名存在')

    @property
    def code(self):
        """获取状态码"""
        return self.value[0]

    @property
    def msg(self):
        """获取状态码信息"""
        return self.value[1]
