from django.db import models
from django.core.validators import MaxValueValidator, RegexValidator
from rest_framework import serializers


class UserModel(models.Model):
    # 左边是模型名，右边db_column是字段名，要不就是同名
    id = models.AutoField(primary_key=True)
    name = models.CharField(
        '用户昵称',
        max_length=20,
        validators=[
            MaxValueValidator(20, '不能大于20字')
        ]
    )
    account = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z0-9]*$',
                message='account must be Alphanumeric',
                code='invalid_account'
            )
        ]
    )
    password = models.CharField(
        max_length=50,
        validators=[]
    )
    create_time = models.DateTimeField()
    update_time = models.DateTimeField()

    # 还可以指定排序字段、索引约束等
    class Meta:
        # 表名
        db_table = 'user'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = '__all__'
