# date:2017/10/4
# author:Kanon

import requests
from bs4 import BeautifulSoup
import time


url1 = 'http://www.jwc.uestc.edu.cn/Index.action'
url2 = 'http://www.jwc.uestc.edu.cn/web/News!find.action'
headers = {'user-agent': 'Mozilla/5.0'}
data = {'k':'游泳测试'}
while True:
    # 向服务器post数据
    r = requests.post(url2, data=data, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    # print(soup.prettify())
    # 根据total这个类名获得记录总数
    a = soup.find_all(class_="total")[0].get_text()
    a = int(a)
    # 查找最近一条记录
    b = soup.find(class_="textAreo clearfix").get_text()
    if a>9:
        print('\n\n')
        print("游泳测试通知已经发布")
        print("最新的公告为：  "+b)
        print('\n\n')
    else:
        print('\n\n')
        print("游泳测试通知还未发布")
        print("最新的公告为："+b)
        print('\n\n')
    time.sleep(7200)
