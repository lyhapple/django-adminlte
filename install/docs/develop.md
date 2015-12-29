### Django快速开发平台开发者文档

## 一、开发规范

###Model

在Model类中定义内部类Config, 根据需要定义以下属性及类方法

* **属性**：

    * *list_template_name (可选)*
        列表模板页
    
    * *form_template_name (可选)*
    ﻿
        ﻿表单模板页
    
    * *detail_template_name (可选)*
    
        详情模板页
    
    * *list_display_fields (必选)*
    
        列表页面模板显示字段集，tuple类型
    
    * *list_form_fields (必选)*
    
        新建或更新模型信息表单页面显示的字段集，tuple类型
    
    * *filter_fields (可选)*
    
        用于过滤数据的字段集，tuple类型，django-rest-framework会使用到此属性的值，
        通过在url中提供参数及值过滤数据, 例如url?status=0
    
    * *search_fields (可选)*
    
    用于查询数据的字段集, tuple类型, django-rest-framework会使用到此属性的值，
    具体可参与django-rest-framework官网文档有关search field章节的内容.
    
    * *success_url (可选)*
    
    表单保存成功后的默认跳转路径
    

* **类方法**, 注意：是类方法,方法名均使用@classmethod装饰器

    * *filter_queryset(cls, queryset, request)   (可选)*
    
        数据过滤函数，针对当前模型的数据集合的过滤扩展方法，例:

            @classmethod
            def filter_queryset(cls, queryset, request):
                return queryset.filter(receiver=request.user).exclude(
                    status=SiteMail.DELETE
                )
                
                
    * *get_object_hook(cls, request, obj)   (可选)*
    
        获取单个模型实例时的勾子方法，可以使用此方法在获取实例对象时对这个实例对象进行操作,
        比如更新数据的读取状态等，例如：
    
            @classmethod
            def get_object_hook(cls, request, obj):
                obj.status = ReadStatus.READ
                obj.save(update_fields=['status'])
                
        
    * *update_object_hook(cls, obj)	(可选)*
    
        更新模型实例时的勾子方法
    
            @classmethod
            def update_object_hook(cls, request, obj):
                obj.creator = request.user
                obj.save()



###Serializer 序列化类

使用了django-rest-framework框架, 所有序列化类参照DRF的官方文档标准即可。

**注意**：需要将serializers模块导入到路径中，可按如下方式进行操作。

为应用添加apps.py模块, 创建app config类，并在ready方法导入serializers模块, 例如：

    class AdminLteAppConfig(AppConfig):
        name = "core.adminlte"
        verbose_name = u"系统管理"
        
        def ready(self):
            import serializers
            pass
        
