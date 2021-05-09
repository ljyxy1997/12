import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
path = 'data/regress_data1.csv'
data = pd.read_csv(path)
data.head() #默认读取前5行数据
data.describe() #计算出数组的个数、平均值、标准差、最小值、25、50、75，最大值
data.plot(kind='scatter', x='人口', y='收益', figsize=(12,8))#kind:图的种类，figsize(a,b):a为X轴长，b为Y轴长
plt.xlabel('人口',fontsize=18) #frontsize:人口字体大小
plt.ylabel('收益', rotation=0, fontsize=18) #rotation:收益字体的旋转角度
plt.show()