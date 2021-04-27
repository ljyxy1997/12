print("hello world")
print("hello\tworld")#\t相当于tab键
print("hello\nworld")#\n相当于回车键
print("hello"+"123")#＋前后一定要是同一类型变量
print("hello"+str(123))#str将数字转成字符串
print("1+2")#打印出的是字符串
print(1+2)#打印出的是结果
print(int('1')+2)#打印出的是结果
print(int(1.5)+2)#打印出的是结果
#print(int('1.5')+2)#出现错误
print(float('1.5')+2)#正确      9这种在C中常用，注意对比10和11，字符串想要转换成数字前面的数据类型一定要准确
print("hello",123)#用逗号即可解决输出前后不一致的问题
print("I'm ok",123)#想要打印单引号则用双引号在最外层
print('He said "I\'m ok"')#想要打印双引号则用单引号在最外层


