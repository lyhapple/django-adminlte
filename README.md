# django-adminlte
##鸣谢lyhapple
    注意: 以下内容基于Mac OSX

## 依赖

* python 2.7
* django 1.8

## 技术栈

* 前端：
    * jquery, vue.js, underscore
    * adminlte 开源前端模板
    
* 后端
    * django
    * django-rest-framework
    * django-mptt
    * django-registration
    

## 准备工作：

推荐使用virutalenv环境

1. pip install virtualenv
2. virtualenv lte
3. source lte/bin/activate
4. cd lte


## 跑起来

1. git clone git@github.com:326029212/django-adminlte.git
2. cd django-adminlte
3. pip install -r requirement.txt
4. python manage_dev.py makemigrations
5. python manage_dev.py migrate
6. python manage_dev.py loaddata install/data/fixture_data.json
7. python manage_dev.py runserver

## 开发与使用

### 开发者文档

请参考 docs/develop.md

如需fork，请去git@github.com:lyhapple/django-adminlte.git请使用develop分支，并向该分支提交 pull request。


### 使用

1. 超管用户名及密码都是: admin

2. django自带后台地址为: /admin/

3. 写好Model 与 serializer 类之后，可以通过菜单管理页面，增加管理入口，
比如，创建了名为demo的app, 然后新增了一个Product Model,
再新增一个ProductSerializer类, 最后即可在菜单管理页面增加对Product数据的管理入口
