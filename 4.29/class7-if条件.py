a=1
b=2
c=3
d=1
if a>b:
    print('right1')
if a>=d:
    print('right2')
if a==d:
    print('right3')
if a!=b:
    print('right4')
if a<b<c:
    print('right5')
if a<b>c:
    print('right6')
if 1<100:
    print('right')
if 1 > 100:
    print('right')
else:
    print('wrong')
#******************* 1、连续if
if a==b:
    print('a==b')
if  a==d:
    print('a==d')
if  a==d:
    print('同上')
#******************* 2、连续elif
if a==b:
    print('a==b')
elif  a==d:
    print('a==d')
elif  a==d:
    print('同上')          #1和2的区别在于，1程序即使中途条件成立它还会继续进行下去，而2只要中间有成立则停止
if a==b:
    print('a==b')
if  a==d:
    pass   #条件成立啥都不做
