import logging
import jwt
from datetime import datetime, timedelta, timezone

from my_common.models.mysql_default.user_model import UserModel

logger = logging.getLogger('django')


class JWTUtil:

    ''' 请求头key '''
    AUTH_HEADER_KEY = "authorization"

    ''' token 前缀 '''
    TOKEN_PREFIX = "Bearer "

    ''' 密钥 '''
    __SECRET = "my_secret"

    ''' 过期时间,单位为秒 '''
    __EXPIRATION = 24 * 60 * 60

    ''' 生成用户token,设置token超时时间 '''
    def create_token(user_model: UserModel):
        shanghai = timezone(timedelta(hours=8))
        exp = datetime.now() + timedelta(seconds=JWTUtil.__EXPIRATION)
        iat = datetime.now()
        # 替换时区
        exp = exp.replace(tzinfo=shanghai)
        iat = iat.replace(tzinfo=shanghai)
        payload = {
            # 过期时间
            'exp': exp,
            # 创建时间
            'iat': iat,
            # payload data
            'data': {
                'id': user_model.id,
                'name': user_model.name,
                'account': user_model.account,
            }
        }
        return jwt.encode(payload, JWTUtil.__SECRET, algorithm='HS256')

    ''' 校验token并解析token '''
    def verify_token_is_valid(token: str):
        try:
            playload = jwt.decode(token, JWTUtil.__SECRET, algorithms="HS256")
        except Exception as exception:
            logger.error("token解码异常: {exp}".format(exp=exception))
            return False
        else:
            return True

    ''' 获取token中的payload '''
    def get_token_playload(token: str):
        playload = None
        try:
            playload = jwt.decode(token, JWTUtil.__SECRET, algorithms="HS256")
        except Exception as exception:
            logger.error("token解码异常: ", exception)
            return None
        else:
            return playload
