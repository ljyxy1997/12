class human: #类
    #类的属性
    name ='someone'
    age =100
    #类的方法
    def my_name(self):
        print('my name is',self.name)
    def my_age(self):
        print('my age is',self.age)
    def eat(self):
        print('eat')
    def think(self,a,b):
        print(a+b)
person1 =human() #创建一个person1的对象
print(person1.name)
person1.name='zhangsan'
print(person1.name)
print(person1.think(1,2))

class human1: #类
    def __init__(self,name,age): #创建对象时会执行
        self.name=name
        self.age=age
    #类的方法
    def my_name(self):
        print('my name is',self.name)
    def my_age(self):
        print('my age is',self.age)
    def eat(self):
        print('eat')
    def think(self,a,b):
        print(a+b)

person2 =human1('xiaoming',10)
print(person2.name)
print(person2.my_name())
print(person2.age)