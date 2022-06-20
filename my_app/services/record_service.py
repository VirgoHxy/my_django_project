from my_common.models.mysql_test.record_model import RecordModel
from my_common.services import RecordService as CommonRecordService


class RecordService():
    commonRecordService = CommonRecordService()

    def get_record_list(self):
        return self.commonRecordService.select_all()

    def get_record_list_pagination(self, data):
        return self.commonRecordService.select_list_pagination(data)

    def get_record_by_id(self, id):
        return self.commonRecordService.select_by_id(id)

    def create_record(self, data):
        model_data = RecordModel(**data)
        return self.commonRecordService.insert_record(model_data)

    def update_record(self, data):
        model_data = RecordModel(**data)
        return self.commonRecordService.update_record(model_data)

    def delete_record_by_id(self, id):
        return self.commonRecordService.delete_by_id(id)
