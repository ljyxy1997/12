a_list=[1,2,3,4,5]
d={'pen':7,'apple':3,'applepen':10} #key:value,键：值
d2={1:'a',5:'b',2:'d'}
d3={1.2:3,'a':3.5,1:'aaa'}
print(d)
print(d2)
print(d3)

print(d['apple'])
print(d2[2])
print(d3[1.2])

d4={'a':[1,2,3,4],'b':(1,2,3,4),'c':{'aa':1,'bb':2}}
print(d4['a'])
print(d4['c']['aa']) #取字典里面的字典

d['pen']=10  #修改key对应的value
print(d)

d['pineapple']=3 #新增一个key：value对，字典是没有顺序的容器
print(d)

del  d['pineapple'] #删除一个键值对
print(d)

for i,j in d.items(): #遍历整个字典的键值对
    print('key',i,'\t','value',j)

for key in d.keys(): #遍历整个字典的键
    print('key:',key)

for value in d.values(): #遍历整个字典的值
    print('value:',value)

for i in sorted(d2.keys()):
    print('key',i)