# coding=utf-8

from django.contrib import admin
from .models import Company, Department, Staff


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    pass
