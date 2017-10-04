# date:2017/10/4
# author:Kanon

import requests
from bs4 import BeautifulSoup

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4'
}
url='http://idas.uestc.edu.cn/authserver/login?service=http%3A%2F%2Fportal.uestc.edu.cn%2F'
urlScore = 'http://eams.uestc.edu.cn/eams/teach/grade/course/person!historyCourseGrade.action?projectType=MAJOR'
# 填入用户名
username = ''
# 填入密码
password = ''

# 建立会话
s = requests.Session()
# 请求登陆页面
pageLogin = s.get(url)
soupLogin = BeautifulSoup(pageLogin.content, "html.parser")
# 登陆参数填充
lt = soupLogin.find('input', {'name':'lt'})['value']
execution = soupLogin.find('input', {'name':'execution'})['value']
parameters = {
    'username':username,
    'password':password,
    'lt':lt,
    'dllt':'userNamePasswordLogin',
    'execution':execution,
    '_eventId':'submit',
    'rmShown':1,
}

# post请求登陆
pageIndex = s.post(url, headers=headers, data=parameters)
# 请求成绩页面
pageScore = s.get(urlScore, headers=headers)
# 解决重复登陆
pageScore = s.get(urlScore, headers=headers)
soupScore = BeautifulSoup(pageScore.content, "html.parser")
print(soupScore.prettify())
