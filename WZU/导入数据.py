import pandas as pd
import numpy as np
path1 = 'data/ex1.txt'
data = pd.read_csv(path1,sep='\t',names=['x0','x1','y'])  #读取用空格隔开的txt数据
n=data.head()
print(n)

path2 = 'data/ex2data1.txt'
data3 = pd.read_csv(path2,sep=',',names=['x0','x1','y'])  #读取用,隔开的txt数据
m=data3.head()
print(m)

path3='data/regress_data1.csv'    #读取csv格式数据
data4=pd.read_csv(path3)
p=data4.head()
print(p)