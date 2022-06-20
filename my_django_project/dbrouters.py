from my_common.models.mysql_test import RecordModel
# from my_common.models.mysql import UserModel


class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        """ reading SomeModel from otherdb """
        if model == RecordModel:
            return 'mysql_test'
        return None

    def db_for_write(self, model, **hints):
        """ writing SomeModel to otherdb """
        if model == RecordModel:
            return 'mysql_test'
        return None
