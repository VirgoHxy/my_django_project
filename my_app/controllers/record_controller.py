from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

from my_common.models.mysql_test.record_model import CreateRecordSerializer, DeleteRecordByIdSerializer, GetRecordByIdSerializer, GetRecordListPaginationSerializer, UpdateRecordSerializer
from my_common.utils.decorator.decorator import token_required, register_decorator, base_response
from my_common.utils.util.serializer_util import CheckParamUtil
from my_common.models.mysql_test import RecordModel, RecordSerializer
from ..services import RecordService


class RecordController(viewsets.ModelViewSet):
    """
    Record操作
    """
    recordService = RecordService()
    queryset = RecordModel.objects.all()
    serializer_class = RecordSerializer

    @swagger_auto_schema(
        operation_summary='查询所有数据'
    )
    @action(detail=False, methods=['get'], url_path='getRecordList')
    @register_decorator(token_required(), base_response())
    def get_record_list(self, request: HttpRequest):
        """
        查询所有数据
        """
        list = self.recordService.get_record_list()
        return JsonResponse(list)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'page_index',
                openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'page_size',
                openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_INTEGER
            )
        ],
        operation_summary='分页查询数据'
    )
    @action(detail=False, methods=['get'], url_path='getRecordListPagination')
    @register_decorator(token_required(), base_response())
    def get_record_list_pagination(self, request: HttpRequest):
        """
        分页查询数据
        """
        CheckParamUtil.is_valid(
            GetRecordListPaginationSerializer,
            request.query_params
        )
        list = self.recordService.get_record_list_pagination(
            request.query_params
        )
        return JsonResponse(list)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_INTEGER
            )
        ],
        operation_summary='通过id查询一行数据'
    )
    @action(detail=False, methods=['get'], url_path='getRecordById')
    @register_decorator(token_required(), base_response())
    def get_record_by_id(self, request: HttpRequest):
        """
        通过id查询一行数据
        """
        CheckParamUtil.is_valid(
            GetRecordByIdSerializer,
            request.query_params
        )
        record = self.recordService.get_record_by_id(
            request.query_params.get('id')
        )
        return JsonResponse(record)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'content': openapi.Schema(type=openapi.TYPE_STRING),
            'type': openapi.Schema(type=openapi.TYPE_STRING)
        },
        required=['content']
    ), operation_summary='创建记录')
    @action(detail=False, methods=['post'], url_path='createRecord')
    @register_decorator(token_required(), base_response())
    def create_record(self, request: HttpRequest):
        """
        创建记录
        """
        CheckParamUtil.is_valid(
            CreateRecordSerializer,
            request.data
        )
        self.recordService.create_record(request.data)
        return HttpResponse(True)

    @swagger_auto_schema(request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'content': openapi.Schema(type=openapi.TYPE_STRING),
            'type': openapi.Schema(type=openapi.TYPE_STRING)
        },
        required=['id', 'content']
    ), operation_summary='更新记录')
    @action(detail=False, methods=['put'], url_path='updateRecord')
    @register_decorator(token_required(), base_response())
    def update_record(self, request: HttpRequest):
        """
        更新记录
        """
        CheckParamUtil.is_valid(
            UpdateRecordSerializer,
            request.data
        )
        self.recordService.update_record(request.data)
        return HttpResponse(True)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                'id',
                openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_INTEGER
            )
        ],
        operation_summary='通过id删除一行数据'
    )
    @action(detail=False, methods=['delete'], url_path='deleteRecordById')
    @register_decorator(token_required(), base_response())
    def delete_record_by_id(self, request: HttpRequest):
        """
        通过id删除一行数据
        """
        CheckParamUtil.is_valid(
            DeleteRecordByIdSerializer,
            request.query_params
        )
        self.recordService.delete_record_by_id(
            request.query_params.get('id')
        )
        return HttpResponse(True)
