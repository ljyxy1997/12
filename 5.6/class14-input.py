a_input=input()
print(a_input)

b_input=input('Please input something:')
print(b_input)

name=input("Please enter your name:")
print('hello',name)

number=input('Please input a number:')
if int(number) >100:
    print('这个数大于100')
elif int(number) ==100:
    print('这个数等于100')
else:
    print('这个数小于100')