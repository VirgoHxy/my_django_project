from functools import wraps


def register_decorator(*decorators):
    def register_wrapper(func):
        for deco in decorators[::-1]:
            func = deco(func)
        func._decorators = decorators
        return func
    return register_wrapper


def token_required(required=True, **other_args):
    def token_decorator(func):
        @wraps(func)
        def with_auth(*args, **kwargs):
            return func(*args, **kwargs)
        return with_auth
    token_decorator._func_name = 'token_required'
    token_decorator._func_param = {'required': required, **other_args}
    return token_decorator


def is_token_required(decorators: list):
    token_required = False
    decorator_list = [
        {
            'func_name': decorator._func_name,
            'func_param': decorator._func_param
        } for decorator in decorators
    ]
    for item in decorator_list:
        func_name = item.get('func_name')
        func_param = item.get('func_param')
        if func_name == 'token_required' and func_param.get('required'):
            token_required = True
            break
    return token_required


def base_response():
    def response_decorator(func):
        @wraps(func)
        def with_reponse(*args, **kwargs):
            return func(*args, **kwargs)
        return with_reponse
    response_decorator._func_name = 'base_response'
    response_decorator._func_param = {}
    return response_decorator


def is_return_base_response(decorators: list):
    return_base_response = False
    decorator_list = [
        {
            'func_name': decorator._func_name,
            'func_param': decorator._func_param
        } for decorator in decorators
    ]
    for item in decorator_list:
        func_name = item.get('func_name')
        func_param = item.get('func_param')
        if func_name == 'base_response':
            return_base_response = True
            break
    return return_base_response
