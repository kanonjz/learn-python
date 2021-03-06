## Django和Spring对比

#### 相同点：
- 都采用MVC的方式来组织代码，将业务逻辑，数据，视图分离开来

#### Django优点
1. 提供了可视化的控制台可以很方便地进行操作
2. ORM映射的这一套机制已经很完善，我们甚至都不需要去写sql语句
3. url配置很方便且优雅
4. Django自带一套安全验证系统，可以进行用户管理和权限控制
5. 提供多种网站防御措施，可以防止sql注入（`sql injection`），跨站请求伪造（`CSRF`：Cross Site Request Forgery），跨站脚本攻击（`XSS`：Cross-site scripting），点击劫持（`Clickjacking`）

#### Django缺点
1. 系统的耦合度高，很难像Spring那样引入第三方库
2. 自带的ORM远没有Mybatis等持久层框架强大

#### Spring优点
1. AOP编程的支持，可以很方便地进行非业务逻辑的控制，非业务逻辑比如日志和安全等功能
2. IoC控制反转，通过Spring提供的IoC容器，我们可以将对象之间的依赖关系交由Spring来管理，方便解耦，简化开发
3. 可以集成各种优秀的框架，比如Mybatis，Hibernate，Shiro，Dubbo
4. 支持声明式事务

#### Spring缺点
1. 框架笨重，有大量的jar包需要导入
2. 配置xml文件非常繁琐

---
### 总结
两个框架都有各自的优缺点，Django的那一套轻便又优雅，很多东西都已经帮你做好了，像一位朝气蓬勃的年轻人；而Spring相比起来就显得有些笨重，但Spring在处理并发以及一些细节上有自己很完善的东西，而且还围绕着一群在某方面能力超群的兄弟，更像是一位富有经验，游走于各式场合，对规则已经轻车熟路的职场老油条。
<br><br>

总的来说，萝卜白菜，各有所爱，根据实际的需求来选择合适的框架，才不会怕“嫁错郎”
