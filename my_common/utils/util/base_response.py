from django.http.response import JsonResponse

from my_common.utils.exception.exception_enum import StatusCodeEnum


class BaseResponse(JsonResponse):
    """ 基于JsonResponse的格式返回定义 """

    def __init__(self, data=None, code=None, msg=None,
                 status=None):

        # 默认成功
        status_enum = StatusCodeEnum.SUCCESS if status == None else StatusCodeEnum[
            status]
        status = int(str(status_enum.code)[:3])
        self.data = {}
        self.data["status"] = True if status_enum.name == 'SUCCESS' else False
        self.data["code"] = code or status_enum.code
        self.data["msg"] = msg or status_enum.msg
        if data != None and data != '':
            self.data["data"] = data
        super(BaseResponse, self).__init__(self.data, status=status)
