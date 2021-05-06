text='Write a text\nhello world'
print(text)
my_file=open('file1.text','w') #以写入的方式打开文件，如果文件不存在会创建该文件
my_file.write(text)
my_file.close()

with open('file2.txt','w') as f2: #清空文件，然后写入
    f2.write('hahaha\n123123')

with open('file2.txt','a') as f2: #在文件最后追加内容
    f2.write(text)

with open('file2.txt','r') as f2: #以读取的方式打开文件
    content=f2.read()             #读取全部内容
    print(content)

with open('file2.txt','r') as f2:
    content = f2.readline()       #读取一行内容
    print(content)

with open('file2.txt','r') as f2:
    content = f2.readlines()       #读取所有行存放到一个列表中
    print(content)

filename ='file2.txt'
with open(filename) as f:
    for line in f:
        print(line)

filename ='file2.txt'
with open(filename) as f:
    for line in f:
        print(line.rstrip())