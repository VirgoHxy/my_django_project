from django.contrib import admin

from .models.mysql_default import UserModel
from .models.mysql_test import RecordModel

admin.site.register(UserModel)
admin.site.register(RecordModel)
