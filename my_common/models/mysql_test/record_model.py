from django.db import models
from django.core.validators import MaxValueValidator, RegexValidator
from rest_framework import serializers

from my_common.utils.util.serializer_util import PaginationSerializer


class RecordModel(models.Model):
    # 左边是模型名，右边db_column是字段名，要不就是同名
    id = models.AutoField(primary_key=True)
    content = models.CharField(
        '字段说明，记录内容',
        db_column='cont',
        max_length=100,
        blank=True,
        validators=[MaxValueValidator(100, '不能大于100字')]
    )
    type = models.CharField(
        max_length=50,
        null=True,
        validators=[RegexValidator]
    )
    create_time = models.DateTimeField(db_column='cr_time')
    update_time = models.DateTimeField(db_column='up_time')

    # 还可以指定排序字段、索引约束等
    class Meta:
        # 表名
        db_table = 'my_record'


class RecordSerializer(serializers.ModelSerializer):

    class Meta:
        model = RecordModel
        # fields = '__all__'
        fields = ['id', 'content', 'type']


class GetRecordListPaginationSerializer(PaginationSerializer):
    pass


class GetRecordByIdSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)


class CreateRecordSerializer(serializers.Serializer):
    content = serializers.CharField(required=True)
    type = serializers.CharField(required=False, allow_blank=True)


class UpdateRecordSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    content = serializers.CharField(required=True)
    type = serializers.CharField(required=False, allow_blank=True)


class DeleteRecordByIdSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
