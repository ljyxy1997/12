a_list=[1,20,30,1,1,1,1]#列表
print(a_list)
print(a_list[2])#打印第二个元素，从左往右，开头为0
print(a_list[-5])#打印倒数第五个元素，从右往左，开头为-1
print(a_list[1:4])#打印1-4这几个元素
print(a_list[:-2])#从头开始打印到倒数第二个元素
print(a_list[-3:])#从倒数第三个元素到结束
for i in a_list:
    print(i)
t=len(a_list)#计算列表长度
print(t)

q=a_list.index(30)#计算元素位置在哪
print(q)

a=a_list.count(1)#计算某个元素有多少个
print(a)

b_list=[1,20,7,3,5,1,8]
b_list.sort()#对列表排序  千万不要写 c=b_list.sort() print(c)得到的结果是none,因为只要用了b_list.sort(),顺序就已经发生变化了。
print(b_list)
c_list=[1,20,7,3,5,1,8]
sorted(c_list)
print(c_list)   #此处结果并未排序
print(sorted(c_list))  #此处结果排序，因为：sorted 不改变原来的排序，只是返回排序后的新排序，且sort只能用于列表

a_list.sort(reverse=True)#倒排序
print(a_list)

