class human: #类
    def __init__(self,name='someone',age=10): #创建对象时会执行
        self.name=name
        self.age=age
        print('human init')
    #类的方法
    def my_name(self):
        print('my name is',self.name)
    def my_age(self):
        print('my age is',self.age)
    def eat(self):
        print('eat')
    def think(self,a,b):
        print(a+b)
class student(human) :#子类继承父类
    def __init__(self,grade=1,school='MIT'):
        super().__init__() #调用父类初始化
        self.grade=grade
        self.school=school
        self.score=100
        print('student init')

    #添加子类自己的方法
    def learn(self):
        print('learning')
    def my_school(self):
        print('my school is',self.school)
    #子类可以重写父亲的方法
    def think(self,a,b):
        print(a-b)
stu2=student()
stu2.eat()
stu2.learn()
print(stu2.name)
stu2.think(1,3)