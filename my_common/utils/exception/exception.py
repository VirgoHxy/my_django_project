from .exception_enum import StatusCodeEnum


class MyBaseException(Exception):
    """公共异常类"""

    def __init__(self, enum: StatusCodeEnum):
        self.code = enum.code
        self.msg = enum.msg
        self.enum_name = enum.name
        super().__init__()


class BusinessException(MyBaseException):
    """业务异常类"""
    __enum = StatusCodeEnum.BUSINESS_ERROR

    def __init__(self, msg=__enum.msg):
        self.code = self.__enum.code
        self.msg = msg
        self.enum_name = self.__enum.name


class TokenException(MyBaseException):
    """token异常类"""

    __enum = StatusCodeEnum.SIGNATURE_NOT_MATCH

    def __init__(self, msg=__enum.msg):
        self.code = self.__enum.code
        self.msg = msg
        self.enum_name = self.__enum.name


class ParamInvaildException(MyBaseException):
    """参数校验异常类"""

    __enum = StatusCodeEnum.BODY_NOT_MATCH

    def __init__(self, msg=__enum.msg):
        self.code = self.__enum.code
        self.msg = msg
        self.enum_name = self.__enum.name
