`linux`
![hello](https://github.com/kanonjz/learn-python/raw/master/django/pictures/1.PNG)
***
### {% csrf_token %}
Since we’re creating a POST form (which can have the effect of modifying data), we need to worry about Cross Site Request Forgeries. Thankfully, you don’t have to worry too hard, because Django comes with a very easy-to-use system for protecting against it. In short, all POST forms that are targeted at internal URLs should use the `{% csrf_token %}` template tag.
***
### `<a href="{% url 'add-2' 3 4 %}">signup</a>`
可以进行传参，add-2是在`urls.py`中定义的名字，生成的url为/add/3/4/
##### 写url其实也可以用hardcoded的方法
`<a href="../polls/pagination">signup</a>`
##### `{% url %}`tag的作用
本质上是为了在变更路径时比较方便，不用到每一个template里修改路径。如果采用hardcoded的方式，修改起来很麻烦
![{% url %}的用法](https://docs.djangoproject.com/en/1.11/intro/tutorial03/)
