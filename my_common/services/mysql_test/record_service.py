from datetime import datetime

from django.forms import model_to_dict

from my_common.utils.util.base_crud import BaseCRUDService
from my_common.models.mysql_test import RecordModel, RecordSerializer


class RecordService(BaseCRUDService):
    def __init__(self, *args, **kwargs):
        super(RecordService, self).__init__(
            model_class=RecordModel, serializer_class=RecordSerializer, *args, **kwargs
        )

    def insert_record(self, model_data: RecordModel):
        model_data.create_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        super(RecordService, self).insert(model_to_dict(model_data))

    def update_record(self, model_data: RecordModel):
        model_data.update_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        super(RecordService, self).update_by_id(model_to_dict(model_data))
