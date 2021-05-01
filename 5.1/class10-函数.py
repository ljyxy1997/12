def function():#定义一个函数
    a=1
    b=2
    c=a+b
    print('a:',a)
    print('b:',b)
    print('c:',c)
    print('a+b:',c)
function()

def function2(a,b): #定义一个带参数函数，a,b为形参（局部变量），只有在函数内部发生作用
    c = a + b
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('a+b:', c)
function2(20,3)

def function3(a=10,b=20): #设置默认值
    c = a + b
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('a+b:', c)
function3()
function3(40)   #把40传给了第一个值

def function4(a,b=20): #设置默认值
    c = a + b
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('a+b:', c)
function4(60)  #60传给a
function4(60,80)  #60传给a,80传给b

a=800
def function5(a=10,b=20): #设置默认值
    c = a + b
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('a+b:', c)
function5() #结果a=10，由此可知，如果函数中的局部变量与全局变量重名，默认使用局部变量

a=800
def function6(b=20):
    global a #使用全局变量
    c = a + b
    print('a:', a)
    print('b:', b)
    print('c:', c)
    print('a+b:', c)
function6() #结果a=10，由此可知，如果函数中的局部变量与全局变量重名，默认使用局部变量

def add(a,b):
    c=a+b
    return c  #即把c返回给add
d=add(1,2)
print(d)
