import random
n=random.randint(1,100)
step=0
high=100
low=1
def get_number():
    guess = input('Please enter a number:')
    while 1:
        if guess.isdigit():
            guess=int(guess)
            return guess
        else:
            guess = input('Please enter a number:')
guess=get_number()
while 1:
    step+=1
    if guess==0:
        break
    print('step',step)
    if guess>n:
        print(guess,'is high')
        high=guess - 1
    elif guess<n:
        print(guess,'is low')
        low=guess+1
    else:
        print('right!')
        break
    print('You can try',low,'to',high)
    guess = get_number()
print('Game over')