# Generated by Django 3.2.6 on 2022-06-15 09:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('content', models.CharField(blank=True, db_column='cont', max_length=100, validators=[django.core.validators.MaxValueValidator(100, '不能大于100字')], verbose_name='字段说明，记录内容')),
                ('type', models.CharField(max_length=50, null=True, validators=[django.core.validators.RegexValidator])),
                ('create_time', models.DateTimeField(db_column='cr_time')),
                ('update_time', models.DateTimeField(db_column='up_time')),
            ],
            options={
                'db_table': 'my_record',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20, validators=[django.core.validators.MaxValueValidator(20, '不能大于20字')], verbose_name='用户昵称')),
                ('account', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_account', message='account must be Alphanumeric', regex='^[a-zA-Z0-9]*$')])),
                ('password', models.CharField(max_length=50)),
                ('create_time', models.DateTimeField()),
                ('update_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]