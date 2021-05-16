import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
path="data/ex1.txt"
data=pd.read_csv(path,sep='\t',names=["x1","x2",'y'])
n=data.head()
cols=data.shape[1]
x=data.iloc[:,1:2]
print(x)
y=data.iloc[:,-1:]
data.plot(kind='scatter', x='x1', y='y', figsize=(12,8)) #第一种方法。注意是data.plot而不是plt.plot,就算已经设定了x，y的值也不行，里面的x、y需要设定你想表示的数值，kind:图的种类，figsize(a,b):a为X轴长，b为Y轴长
plt.show()
plt.scatter(x, y)#第二种方法。括号前是图的种类
plt.xlabel('人口',fontsize=18) #frontsize:人口字体大小
plt.ylabel('收益', rotation=0, fontsize=18) #rotation:收益字体的旋转角度
plt.show()
