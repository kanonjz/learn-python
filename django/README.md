`linux`
![hello](https://github.com/kanonjz/learn-python/raw/master/django/pictures/1.PNG)
### {% csrf_token %}
Since we’re creating a POST form (which can have the effect of modifying data), we need to worry about Cross Site Request Forgeries. Thankfully, you don’t have to worry too hard, because Django comes with a very easy-to-use system for protecting against it. In short, all POST forms that are targeted at internal URLs should use the `{% csrf_token %}` template tag.
### <a href="{% url 'add-2' 3 4 %}">signup</a>
这里的url还有待理解，涉及到reverse（）函数。可以进行传参，生成的url为/add/3/4/
