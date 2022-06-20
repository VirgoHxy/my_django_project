from dataclasses import dataclass
from django.db import models
from django.core.paginator import Paginator
from rest_framework import serializers

from my_common.utils.exception.my_exception import BusinessException


class BaseCRUDMapper():
    __model_class: models.Model

    def __init__(self, model_dict):
        self.__model_class = model_dict

    def insert(self, model_dict):
        return self.__model_class.objects.create(**model_dict)

    def delete_by_id(self, id):
        return self.__model_class.objects.get(pk=id).delete()

    def update_by_id(self, model_dict):
        not_have_none_dict = {k: v for k,
                              v in model_dict.items() if v is not None}
        return self.__model_class.objects.filter(pk=model_dict[self.__model_class._meta.pk.name]).update(**not_have_none_dict)

    def update(self, filter, model_dict):
        not_have_none_dict = {k: v for k,
                              v in model_dict.items() if v is not None}
        return self.__model_class.objects.filter(**filter).update(**not_have_none_dict)

    def select_by_id(self, id):
        return self.__model_class.objects.get(pk=id)

    def select_one(self, filter):
        return self.__model_class.objects.get(**filter)

    def exist(self, filter):
        return self.__model_class.objects.filter(**filter).exists()

    def select_count(self, filter):
        return self.__model_class.objects.filter(**filter).count()

    def select_list(self, filter):
        return self.__model_class.objects.filter(**filter)

    def select_all(self):
        return self.__model_class.objects.all()


class BaseCRUDService():
    __serializer_class: serializers.ModelSerializer
    __model_class: models.Model

    def __init__(self, model_class, serializer_class):
        self.__model_class = model_class
        self.__serializer_class = serializer_class
        self.__mapper = BaseCRUDMapper(model_class)
        # self.__page = {'page_index': int, 'page_size': int}

    def insert(self, model_dict):
        self.__mapper.insert(model_dict)

    def delete_by_id(self, id):
        if not self.__mapper.exist({'pk': id}):
            raise BusinessException('数据不存在!')
        self.__mapper.delete_by_id(id)

    def update_by_id(self, model_dict):
        if not self.__mapper.exist({'pk': model_dict[self.__model_class._meta.pk.name]}):
            raise BusinessException('数据不存在!')
        self.__mapper.update_by_id(model_dict)

    def update(self, filter, model_dict):
        self.__mapper.update(filter, model_dict)

    def select_by_id(self, id):
        if not self.__mapper.exist({'pk': id}):
            raise BusinessException('数据不存在!')
        queryobj = self.__mapper.select_by_id(id)
        serializer = self.__serializer_class(queryobj)
        return serializer.data

    def select_one(self, filter):
        if not self.__mapper.exist(filter):
            raise BusinessException('数据不存在!')
        queryobj = self.__mapper.select_one(filter)
        serializer = self.__serializer_class(queryobj)
        return serializer.data

    def select_count(self, filter):
        return self.__mapper.select_count(filter)

    def select_list(self, filter):
        queryset = self.__mapper.select_list(filter)
        serializer = self.__serializer_class(queryset, many=True)
        return serializer.data

    def select_all(self):
        queryset = self.__mapper.select_all()
        serializer = self.__serializer_class(queryset, many=True)
        return serializer.data

    def select_list_pagination(self, data):
        page = {'page_index': int(data['page_index']),
                'page_size': int(data['page_size'])}
        filter = data.copy()
        del filter['page_index']
        del filter['page_size']
        queryset = self.__mapper.select_list(filter)
        serializer = self.__serializer_class(queryset, many=True)
        paginator = Paginator(serializer.data, page.get('page_size'))
        contacts = paginator.get_page(page.get('page_index') + 1)
        result = {}
        result['count'] = contacts.paginator.count
        result['page'] = contacts.paginator.num_pages
        result['list'] = contacts.object_list
        return result
