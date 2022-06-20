import logging

from django.db import DatabaseError
from django.http import HttpRequest, HttpResponse
from django.middleware.common import MiddlewareMixin

from my_common.utils.decorator.decorator import is_return_base_response, is_token_required
from my_common.utils.util.jwt_util import JWTUtil
from my_common.utils.util.base_response import BaseResponse
from my_common.utils.exception.my_exception import ParamInvaildException, StatusCodeEnum, BusinessException, TokenException

logger = logging.getLogger('django')


class CommonMiddleware(MiddlewareMixin):
    """统一处理中间件"""

    def process_view(self, request: HttpRequest, view_func, view_args, view_kwargs):
        """
        统一处理请求
        :param request: 请求对象
        :return:
        """
        try:
            try:
                decorators = getattr(
                    view_func.cls, list(view_func.actions.values())[0]
                )._decorators
            except AttributeError:
                return None
            token_required = is_token_required(decorators)
            return_base_response = is_return_base_response(decorators)
            if return_base_response:
                request.base_reponse = True
            if token_required:
                try:
                    token = request.headers['Authorization']
                    if token.isspace():
                        raise Exception()
                    token = token if not token.startswith(
                        JWTUtil.TOKEN_PREFIX
                    ) else token[7:]
                    isValid = JWTUtil.verify_token_is_valid(token)
                    if not isValid:
                        raise Exception()
                except:
                    raise TokenException()
        except Exception as exception:
            return self.process_exception(request, exception)

    def process_response(self, request: HttpRequest, response: HttpResponse):
        """
        统一处理响应
        :param request: 请求对象
        :param response: 响应对象
        :return:
        """
        try:
            return_base_response = request.base_reponse
        except:
            return_base_response = False
        if return_base_response:
            if isinstance(response, BaseResponse):
                return response
            elif response.status_code != 200:
                try:
                    code = response.status_code
                    detail = response.data['detail']
                    if code == 405:
                        return BaseResponse(status=StatusCodeEnum.METHOD_NOT_ALLOWED.name, msg=detail)
                    else:
                        return response
                except Exception as exception:
                    return BaseResponse(status=StatusCodeEnum.INTERNAL_SERVER_ERROR.name, msg=repr(exception))
            else:
                data = str(
                    response.content, encoding='utf-8'
                ) if response.content != None else None
                data = eval(data) if data != '' else None
                return BaseResponse(data)
        else:
            return response

    def process_exception(self, request: HttpRequest, exception: Exception):
        """
        统一处理视图异常
        :param request: 请求对象
        :param exception: 异常对象
        :return:
        """
        if isinstance(exception, BusinessException):
            # 业务异常
            return BaseResponse(status=exception.enum_name, msg=exception.msg)

        elif isinstance(exception, TokenException):
            # token异常
            return BaseResponse(status=exception.enum_name, msg=exception.msg)

        elif isinstance(exception, ParamInvaildException):
            # 请求数据异常
            return BaseResponse(status=exception.enum_name, msg=exception.msg)

        elif isinstance(exception, DatabaseError):
            # 数据库异常
            logger.error(repr(exception), exc_info=True)
            return BaseResponse(status=StatusCodeEnum.DB_SERVER_ERROR.name, msg=repr(exception))

        elif isinstance(exception, AttributeError):
            # object没有获取属性异常
            logger.error(repr(exception), exc_info=True)
            return BaseResponse(status=StatusCodeEnum.INTERNAL_SERVER_ERROR.name, msg=repr(exception))

        elif isinstance(exception, Exception):
            # 异常基类
            logger.exception(repr(exception), exc_info=True)
            return BaseResponse(status=StatusCodeEnum.INTERNAL_SERVER_ERROR.name, msg=repr(exception))

        return None
