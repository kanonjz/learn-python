# itchat
无意中发现一个有意思的开源项目itchat，可以获取微信的数据，功能还有待探索,比如计算好友男女比例，获取所有人的签名，制作成词云等等
#### 安装
```
pip install itchat
```
#### 在控制台登录微信并发送消息给filehelper
```
import itchat
# 登录
itchat.login()
#  发送消息
itchat.send(u'你好', 'filehelper')
```
#### 获取好友,friends本质上是一个列表
```
# 获取好友列表
friends = itchat.get_friends(update=True)[0:]
```
