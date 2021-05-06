a=1
b=2
c=3
d=1
if a>b and a==d:
    print('right')
if a<b and a==d:
    print('right')
if a>b or a==d:
    print('right')   #or两边只要一个成立即可，and两边都需成立

colors=['red','blue','black','green']
for color in colors:
    if color=='black':
        print('black')
    else:
        print('not black')

#*********************
for color in colors:
    if color=='black':
        break         #跳出大循环,相当于它所在的循环以后都不执行了
        print('black')
    else:
        print('not black1')

#*********************
for color in colors:
    if color=='black':
        continue         #跳出单次循环，相当于所在循环只有这一次不执行，下次继续。
        print('black')
    else:
        print('not black2')

if 'red' in colors:#判断列表中是否有red，返回值是true false
    print('red')

null=[]
if null: #判断列表是否为空，有值返回true,空的返回false
    print(1)
else:
    print(0)

if 'ann'<'bgg':  #由于第一个字符b大于a所以成立
    print(1)
else:
    print(0)

number=input('Please input a number:')
if int(number) >100:
    print('这个数大于100')
elif int(number) ==100:
    print('这个数等于100')
else:
    print('这个数小于100')   #if if第一个if成立了还得继续判断第二个if是否成立，if,elif第一个if成立了直接结束程序

