# coding=utf-8

from django.contrib import admin
from organization.models import Company, Department, Staff


class CompanyAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    pass


class StaffAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Staff)