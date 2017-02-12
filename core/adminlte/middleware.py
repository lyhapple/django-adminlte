#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals
from django.http import HttpResponse
from core.adminlte.models import Permission, Menu

__author__ = 'lyhapple'


class ApiPermissionCheck(object):
    def process_request(self, request):
        if not request.user.is_superuser and \
                request.path_info.startswith('/api/'):
            # todo: cache
            permissions = Permission.objects.filter(
                group__in=request.user.groups.all()
            )
            resources = []
            for p in permissions:
                resources.append(list(p.resources.values_list('url', flat=True)))                                       #需要转化成list 才行
            for List in resources:
                if type(List) != list:
                    if str(request.path_info) != str(List):
                        return HttpResponse(status=403)
                else:
                    if request.path_info not in List:
                        return HttpResponse(status=403)

class MenuMiddleware(object):
    def process_template_response(self, request, response):
        # todo: cache
        if request.path_info.startswith('/page/') or request.path_info == '/':
            if request.user.is_superuser:
                page_menus = Menu.objects.filter(status=Menu.USABLE)
            else:
                groups = request.user.groups.all()
                permission = Permission.objects.filter(
                    group__in=groups
                ).first()
                page_menus = permission.menus.all()
            response.context_data['page_menus'] = page_menus
        return response