## login() takes 1 positional argument but 2 were given
再自己写login的view的时候出现了这个问题，原因是view的命名和系统自带的auth login function一样，所以得修改login这个名字

## NoReverseMatch at /signup/. Reverse for 'login' not found. 'login' is not a valid view function or pattern name.
在view的名字前加上namespace， 如polls：login
