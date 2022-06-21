# 意见与说明

- 首先个人主观说明，python 不适合去做后台 api 接口，它的设计理念很难舒适的去做 api 的增删改查
- 推荐 api 开发使用 nodejs 或者 java，这两个在 api 的开发中再搭配其他框架会非常舒适，有 TS 基础再学习 JAVA 非常友好
- 目前项目基本上都是前后端分离，所以并不能使用 MVT 的架构，所以本项目还是采用 MVCS 架构，基本设计理念和结构分层按照 springboot + python 设计

# 依赖说明

- Django==3.2.6 -- web 后端框架
- django-rest-swagger==2.2.0 -- api 文档
- django-cors-headers==3.7.0 -- 设置请求头
- djangorestframework==3.12.4 -- rest api
- django-apscheduler -- 定时任务
- drf-yasg==1.20.0 -- api 文档
- PyJWT==2.4.0 -- jwt
- mysqlclient==2.0.3 -- mysql

## 基于 python 架构理念

### 项目的基本目录结构

- 你的 project 名/ -- 项目文件目录
  - \_\_init\_\_.py -- 识别一个目录为一个包的必要条件，下列省略\_\_init\_\_.py 的说明
  - asgi.py -- 基于 ASGI 的 web 服务器进入点，提供异步的网络通信功能，不用管
  - dbrouters.py -- 根据路由匹配 DB
  - settings.py -- **项目的配置文件(重要)**
  - urls.py -- 路由文件，所有的访问都是从这里开始分配，包括 api 和 admin 界面等
  - views.py -- 视图文件，可以理解为 controller
  - wsgi.py -- 基于 WSGI 的 web 服务器进入点，提供底层的网络通信功能，不用管
- 你的 app 名/ -- 应用文件目录，一般为一个模块，例如：用户的增删改查，可以添加一个叫 user 的应用
  - migrations/ -- 用以存储 django 中的 model 类的变化
  - admin.py -- admin 管理工具页面配置，可以用界面方式管理模型
  - apps.py -- 应用的配置文件
  - models.py -- 应用的模型文件
  - services.py -- 实际业务文件
  - tests.py -- 测试文件
  - urls.py -- 应用路由文件
  - views.py -- 控制器文件
- manage.py -- manage.py 接受的是 Django 提供的内置命令，能够方便执行 django 的命令
- requirements.txt -- 项目依赖

## 基于 springboot 架构理念(该项目采用此架构)

### 项目的基本目录结构

- 你的 project 名/ -- 项目文件目录
  - \_\_init\_\_.py -- 识别一个目录为一个包的必要条件，下列省略\_\_init\_\_.py 的说明
  - asgi.py -- 基于 ASGI 的 web 服务器进入点，提供异步的网络通信功能，不用管
  - dbrouters.py -- 根据路由匹配 DB
  - settings.py -- **项目的配置文件(重要)**
  - urls.py -- 路由文件，所有的访问都是从这里开始分配，包括 api 和 admin 界面等
  - views.py -- 视图文件，可以理解为 controller
  - wsgi.py -- 基于 WSGI 的 web 服务器进入点，提供底层的网络通信功能，不用管
- 你的 app 名/ -- 应用文件目录，该目录主要提供实际业务的 controller 和 service
  - controllers/ -- 控制器目录
  - services/ -- 控制器方法对应的业务目录，它组合公共目录的多个 service 的增删改查来达到实际业务
  - apps.py -- 应用的配置文件
  - tests.py -- 测试文件
  - urls.py -- 应用路由文件
- 公共目录名/ -- 也是应用文件目录，该目录主要提供模型、模型基础的 service（基础的增删改查）、工具方法等，不涉及业务或者包含一丢丢业务
  - migrations/ -- 用以存储 django 中的 model 类的变化
  - models/ -- 数据库模型
  - services/ -- 基础的增删改查
  - utils/ -- 工具配置等目录
    - decorator/ -- 装饰器目录
    - exception/ -- 错误异常目录
    - middle/ -- 中间件目录
    - util/ -- 工具目录
  - admin.py -- admin 管理工具页面配置，可以用界面方式管理模型
  - apps.py -- 应用的配置文件
  - tests.py -- 测试文件
- manage.py -- manage.py 接受的是 Django 提供的内置命令，能够方便执行 django 的命令
- requirements.txt -- 项目依赖

### 初始化 django 项目的步骤

- 创建项目
  - django-admin startproject my_django_project
- 进入该项目目录
  - cd my_django_project
- 创建应用
  - python manage.py startapp my_app
  - 添加应用名到 settings.py 的 INSTALLED_APPS
- 安装所需依赖
  - 通过 pip 安装依赖，注意使用虚拟环境保持依赖的干净
  - 通过 pip 生成 requirements.txt -- pip freeze > requirements.txt / 使用 pipreqs
  - 其他即可通过 pip 一键安装依赖 -- pip install -r requirements.txt
- 配置项目数据库
  - 修改 settings.py 的 DATABASES
  - python manage.py migrate
  - 添加模型到 my_app 的 models.py
  - python manage.py makemigrations my_app -- 创建模型记录
  - python manage.py sqlmigrate my_app 0001 -- 查看模型的变更 sql
  - python manage.py migrate -- 真正执行 sql
- 配置 admin 站点
  - python manage.py createsuperuser -- 创建 admin 站点账号
- 配置应用 controller 层
  - 配置 urls.py 中的路由
  - 配置 views.py 的方法
- 配置应用 service 层
  - 配置 service.py 这里写实际的业务
  - Entry.objects.create() -- 增
  - Entry.objects.delete() -- 删
  - Entry.objects.update() -- 改
  - Entry.objects.all() -- 查所有
  - Entry.objects.get() -- 查单个
  - Entry.objects.filter() -- 过滤不符条件的
  - Entry.objects.exclude() -- 与 filter 相反
- 启动项目
  - python manage.py runserver 或者 python manage.py runserver 8080

# question list

- django 框架让请求末尾必须加个斜线，框架好像做了一层重定向，使用配置不加后又会出现其他问题
- vscode 无法支持插件的提示，如 restframework 和 drf-yasg 都是没有提示的
- \_\_init\_\_.py 太多问题，能否不使用\_\_init\_\_.py 定义为包，并能够正常 import
- dbrouters，需要手动判断 router 的一个模型属于那个 db，能否通过一个条件判断一系列模型属于那个 db

# solved question list

- 文件夹复杂难以引包问题，以及引包点过多问题，到底是用相对引入还是绝对引入
  - 当文件夹复杂后，如果使用相对路径引入，则会造成路径会出现很多个点，所以在层级超过两个点的统一用绝对引入
  - 层级在两个点以及以下的用相对引入

# to-do list

# done list

- 错误的统一处理，请求统一处理，响应统一处理 -- 使用中间件和装饰器
- 请求的参数的文档生成 drf-yasg + swagger
- service 重复方法使用继承，并采用 mapper + base_service + service
