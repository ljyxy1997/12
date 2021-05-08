
 #file=open('hahaha','r+')#r+代表先去读取一个文件，如果能打开的话就可以写入

try:
    file=open('hahaha','r+')
except Exception as e:
    print(e)

try:
    file=open('hahaha','r+')
except Exception as e:
    print(e)
    response = input('Do you want to creat it:')
    if(response=='yes'):
        with open('hahaha','w') as f:
            pass
        print('The file was created sucessfully')
    else:
        pass
else:#没有错误
    file.write('hahaha')
    file.close()