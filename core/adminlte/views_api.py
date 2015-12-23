# coding=utf-8

import sys
from rest_framework import filters

from rest_framework.generics import ListCreateAPIView
from core.adminlte.views import get_app_model_name, get_model_content_type

__author__ = 'lyhapple'


class CommonListAPIView(ListCreateAPIView):
    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)

    def get(self, request, *args, **kwargs):
        self.app_name, self.model_name = get_app_model_name(kwargs)
        model_type = get_model_content_type(self.app_name, self.model_name)
        self.model = model_type.model_class()

        serialize_name = self.model.__name__ + 'Serializer'
        module_str = 'core.%s.serializers' % self.app_name
        if module_str not in sys.modules:
            module_str = 'apps.%s.serializers' % self.app_name
        serializer_module = sys.modules[module_str]

        self.queryset = self.model.objects.all()
        self.filter_fields = getattr(self.model.Config, 'filter_fields', ())
        self.search_fields = getattr(self.model.Config, 'search_fields', ())
        self.serializer_class = getattr(serializer_module, serialize_name)

        return super(CommonListAPIView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        q = super(CommonListAPIView, self).get_queryset()
        if hasattr(self.model.Config, 'filter_queryset'):
            q = self.model.Config.filter_queryset(self.request, q)
        return q
