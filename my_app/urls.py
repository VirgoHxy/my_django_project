from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from .controllers import RecordController

# urlpatterns = [
#     path('record/getList', RecordController.get_record_list(), name='get_record_list'),
#     path('record/getById', RecordController.get_record_by_id(), name='get_record_by_id'),
# ]

router = routers.DefaultRouter()
router.get_api_root_view().cls.__name__ = "API Root"
router.get_api_root_view().cls.__doc__ = "API操作能力"
router.register('record', RecordController, 'RecordController')

schema_view = get_schema_view(
    openapi.Info(
        title="API",
        default_version='v1',
        description="",
        terms_of_service="",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
