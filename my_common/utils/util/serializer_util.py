from rest_framework import serializers
from my_common.utils.exception.my_exception import ParamInvaildException


class CheckParamUtil:

    def is_valid(serializer_class: serializers.Serializer, data):
        serializer = serializer_class(data=data)
        if serializer.is_valid() is not True:
            raise ParamInvaildException(serializer.errors)


class PaginationSerializer(serializers.Serializer):
    page_index = serializers.IntegerField(required=True)
    page_size = serializers.IntegerField(required=True)
