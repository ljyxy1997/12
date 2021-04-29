a_list=[1,2,30,30,30,4,2]
print(a_list)
a_list[0]=100#修改列表中第0个元素
print(a_list)

a_list.append(200)#列表最后加元素
print(a_list)

a_list.insert(2,300)#在列表中插入一个元素
print(a_list)

del a_list[2]#删除列表第2个元素
print(a_list)

a_list.remove(30)#删除一个叫30的元素
print(a_list)

a=a_list.pop()#弹出列表中最后一个元素
print(a)
print(a_list)

b_list=[[1,2],[4,5],[7,8]]
print(b_list[1])
print(b_list[2][1])