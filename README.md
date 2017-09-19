# learn-python
1. 一行代码开启简单python服务器 python -m http.server 1234（可以自定义端口号，默认8000）
2. 控制台输入pip show Django可以查看Django的安装路径，其它安装包类似
3. windows远程连接阿里云方式：用ssh秘钥进行匹配
  教程：![使用 SSH 密钥对连接 Linux 实例](https://help.aliyun.com/document_detail/51798.html?spm=5176.doc51792.2.6.DAXO8s)
  putty错误：connection timeout
  错误原因：未添加安全组规则，使外部能够访问22端口
  ![安全组规则配置](https://help.aliyun.com/document_detail/25475.html?spm=5176.2020520101.121.1.6029e411vFxRUf)
  ![Linux 实例 SSH 连接安全组设置](https://help.aliyun.com/knowledge_detail/52086.html)
  如果还不行，排查是否启动ssh服务![ssh服务启动教程](https://yq.aliyun.com/articles/131764)
