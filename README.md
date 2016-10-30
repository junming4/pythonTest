## 把我的项目提交到github 中git remote add origin https://github.com/junming4/tptest.git
## 简介
##该项目使用python 中的django框架测试
    - 安装django 步骤 git clone https://github.com/django/django.git
    - cd django 执行命令 python setup install
    - 创建项目 :  django-admin startproject pythonTest [pythonTest是项目名]
    - 启动 django 测试项目: python manage.py runserver
    - 指定端口启动:python manage.py runserver 0.0.0.12:8080
## django 文件介绍
    -settings.py 文件配置
    -urls.py 路由配置
    -wsgi.py 与apache等服务器对接的接口

## 创建应用
   - django-admin startapp blog
   - 然后在 settings.py 添加一个应用 中INSTALLED_APPS=》blog


    