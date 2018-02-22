# learn-python
1. 一行代码开启简单python服务器 python -m http.server 1234（可以自定义端口号，默认8000）
2. 控制台输入pip show Django可以查看Django的安装路径，其它安装包类似
3. windows远程连接阿里云方式：用ssh秘钥进行匹配
   教程：[使用 SSH 密钥对连接 Linux 实例](https://help.aliyun.com/document_detail/51798.html?spm=5176.doc51792.2.6.DAXO8s)
   
   putty显示错误：connection timeout
   
   错误原因：未添加安全组规则，使外部能够访问22端口
   
   [安全组规则配置](https://help.aliyun.com/document_detail/25475.html?spm=5176.2020520101.121.1.6029e411vFxRUf)
   [Linux 实例 SSH 连接安全组设置](https://help.aliyun.com/knowledge_detail/52086.html)
   如果还不行，排查是否启动ssh服务[ssh服务启动教程](https://yq.aliyun.com/articles/131764)
## Linux下安装python
[教程1](http://www.linuxidc.com/Linux/2016-04/129784.htm) [教程2](http://blog.csdn.net/hobohero/article/details/54381475)

## [Virtualenv](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000)

## 多进程、管道、队列
[参考文章](http://python.jobbole.com/82045/)

## python namespace（LEGB规则）
**Local**：函数、方法内部的局部变量  
**Enclosing**：如果有嵌套函数，内层函数就会搜索外层函数的namespace，该namespace对内层函数而言既非局部也非全局。  
**Global**：当前模块下的全局变量  
**Built-in**：python内建的关键字和变量  

## 函数式编程
![函数式编程](http://oyrpkn4bk.bkt.clouddn.com/%E5%87%BD%E6%95%B0%E5%BC%8F%E7%BC%96%E7%A8%8B.png)  
[廖雪峰：函数式编程](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317848428125ae6aa24068b4c50a7e71501ab275d52000)
[函数式编程（Functional Programming）简介](http://janfan.cn/chinese/2015/05/18/functional-programming.html)  

优点：  
1. 每个函数的执行没有副作用。函数所有功能就是返回一个新的值，没有其他行为，尤其是不得修改外部变量的值。因此在多线程中就没有涉及到共享变量，可以实现无锁的并发。
2. 抽象层度高，利于复用

