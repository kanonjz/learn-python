# 这是关于在django的project中添加名为calculator的app,同时这里也涉及到两种url传参的方式
### 创建app
在project的根目录下执行
```
python manage.py startapp calculator
```
### 添加已安装app
在`settings.py`的`INSTALLED_APPS `添加
```
'calculator.apps.CalculatorConfig',
```
### 编写`views.py`文件
```
from django.shortcuts import render
from django.http import HttpResponse

def add_1(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add_2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))
```
### 在project的`urls.py`添加url
```
from calculator import views as calculator_views

url(r'^add/$', calculator_views.add_1, name='add-1'),
url(r'^add/(\d+)/(\d+)/$', calculator_views.add_2, name='add-2'),
```
### 两种传参方式
`/add/?a=3&b=4` `/add/3/4`
