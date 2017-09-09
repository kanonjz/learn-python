`linux`
![hello](https://github.com/kanonjz/learn-python/raw/master/django/pictures/1.PNG)
***
### {% csrf_token %}
Since we’re creating a POST form (which can have the effect of modifying data), we need to worry about Cross Site Request Forgeries. Thankfully, you don’t have to worry too hard, because Django comes with a very easy-to-use system for protecting against it. In short, all POST forms that are targeted at internal URLs should use the `{% csrf_token %}` template tag.
***
### `<a href="{% url 'add-2' 3 4 %}">signup</a>`
可以进行传参，add-2是在`urls.py`中定义的名字，生成的url为/add/3/4/
#### 写url其实也可以用hardcoded的方法
`<a href="../polls/pagination">signup</a>`
#### `{% url %}`tag的作用
本质上是为了在变更路径时比较方便，不用到每一个template里修改路径。如果采用hardcoded的方式，修改起来很麻烦
![{% url %}的用法](https://docs.djangoproject.com/en/1.11/intro/tutorial03/)

***

### app_name = 'polls'
The tutorial project has just one app, polls. In real Django projects, there might be five, ten, twenty apps or more. How does Django differentiate the URL names between them? For example, the polls app has a detail view, and so might an app on the same project that is for a blog. How does one make it so that Django knows which app view to create for a url when using the {% url %} template tag?

The answer is to add namespaces to your URLconf. In the polls/urls.py file, go ahead and add an app_name to set the application namespace:
```
app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    url(r'^$', polls_views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', polls_views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', polls_views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', polls_views.vote, name='vote'),
    # ex：/polls/pagination/
    url(r'^pagination/$', polls_views.pagination, name='pagination'),
]
```
Now change your polls/index.html template from:
```
<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```
to point at the namespaced detail view:
```
<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```

***

### include（）
In mysite/urls.py, add an import for django.conf.urls.include and insert an include() in the urlpatterns list, so you have:
```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
```
The include() function allows referencing other URLconfs. Note that the regular expressions for the include() function doesn’t have a $ (end-of-string match character) but rather a trailing slash. Whenever Django encounters include(), it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

The idea behind include() is to make it easy to plug-and-play URLs. Since polls are in their own URLconf (polls/urls.py), they can be placed under “/polls/”, or under “/fun_polls/”, or under “/content/polls/”, or any other path root, and the app will still work.

