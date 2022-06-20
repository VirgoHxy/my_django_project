from my_common.utils.util.base_crud import BaseCRUDService
from my_common.models.mysql_default import UserModel, UserSerializer


class UserService(BaseCRUDService):
    def __init__(self, *args, **kwargs):
        super(UserService, self).__init__(
            model_class=UserModel, serializer_class=UserSerializer, *args, **kwargs
        )
