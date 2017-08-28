# x=sint y=cost+(sint)^(2/3)  很标准的爱心

import matplotlib.pyplot as plt  
from matplotlib import animation  
import numpy as np  
import math  
  
  
def drawHeart():  
    t = np.linspace(0, math.pi, 1000)  
    x = np.sin(t)  
    y = np.cos(t) + np.power(x, 2/3)
    plt.plot(x, y, color='red', linewidth=2, label='h')  
    plt.plot(-x, y, color='red', linewidth=2, label='-h')  
    plt.xlabel('t')  
    plt.ylabel('h')  
    plt.ylim(-2, 2)  
    plt.xlim(-2, 2)  
      
    plt.legend()  
    plt.show()  
  
drawHeart() 

====================================================================
# x=(1-sinθ)*cosθ  y=(1-sinθ)*sinθ 胖爱心

import matplotlib.pyplot as plt  
from matplotlib import animation  
import numpy as np  
import math  
  
  
def drawHeart():  
    t = np.linspace((1/2)*math.pi, (-1/2)*math.pi, 1000)  
    x = (1-np.sin(t) )* np.cos(t)
    y = (1-np.sin(t) )* np.sin(t)
    plt.plot(x, y, color='red', linewidth=2, label='h')  
    plt.plot(-x, y, color='red', linewidth=2, label='-h')  
    plt.xlabel('t')  
    plt.ylabel('h')  
    plt.ylim(-2, 2)  
    plt.xlim(-2, 2)  
      
    plt.legend()  
    plt.show()  
  
drawHeart() 

=====================================================================
# x=cosθ  y=cosθ-sinθ 一半椭圆，关于y轴取对称
import matplotlib.pyplot as plt  
from matplotlib import animation  
import numpy as np  
import math  
  
  
def drawHeart():  
    t = np.linspace((1/2)*math.pi, (-1/2)*math.pi, 1000)  
    x = np.cos(t)
    y = np.cos(t)-np.sin(t)
    plt.plot(x, y, color='red', linewidth=2, label='h')  
    plt.plot(-x, y, color='red', linewidth=2, label='-h')  
    plt.xlabel('t')  
    plt.ylabel('h')  
    plt.ylim(-2, 2)  
    plt.xlim(-2, 2)  
      
    plt.legend()  
    plt.show()  
  
drawHeart()

========================================================================
参考：![不错的几个心形曲线] (http://blog.sina.com.cn/s/blog_532affea01014iel.html)
     linspace函数用法  http://blog.csdn.net/grey_csdn/article/details/54561796
     power函数用法  http://blog.csdn.net/lql0716/article/details/52910812?locationNum=2&fps=1
     matplotlib  tutorial https://matplotlib.org/users/pyplot_tutorial.html
     
     
