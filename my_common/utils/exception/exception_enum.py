from enum import Enum


class StatusCodeEnum(Enum):
    """
    状态码枚举类
    规则: 前三位为httpCode，也就是http状态码，后三位为自定义状态码用于快速定位错误
    """

    SUCCESS = (200000, '成功!')
    BUSINESS_ERROR = (200001, '业务错误!')
    BODY_NOT_MATCH = (400000, '请求的数据或格式不符合!')
    SIGNATURE_NOT_MATCH = (401000, '请求的签名不匹配!')
    NOT_FOUND = (404000, '未找到该资源!')
    METHOD_NOT_ALLOWED = (405000, '请求方法类型不符合!')
    INTERNAL_SERVER_ERROR = (500000, '服务器内部错误!')
    DB_SERVER_ERROR = (500001, '服务器内部错误!')
    SERVER_BUSY = (503000, '服务器正忙，请稍后再试!')

    @property
    def code(self):
        """获取状态码"""
        return self.value[0]

    @property
    def msg(self):
        """获取状态码信息"""
        return self.value[1]
