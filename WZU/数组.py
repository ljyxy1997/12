import numpy as np
import pandas as pd
a=np.zeros((28,1))#用zeros生成数组是小括号
g=np.zeros((1,28))
b=np.array([[1,2,3],[2,3,4]])#用array是中括号
c=a[1:]#其实是a[1:，]即从第二行开始，列全取
d=b[1:,:]#调用也是中括号
print(a)
print('c',c)
print('d',d)
print(len(b))#默认打印行数
a=np.insert(a, 0, 1, axis=1)
#np.insert(arr, obj, values, axis)
#arr原始数组，可一可多，obj插入元素位置，values是插入内容，axis是按行按列插入。axis=0是行


print('a',a)
#np.insert(arr, obj, values, axis)
#arr原始数组，可一可多，obj插入元素位置，values是插入内容，axis是按行按列插入。

