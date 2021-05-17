import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
path='data/ex2data1.txt'
data=pd.read_csv(path,sep=',',names=['Exam 1','Exam 2','Admitted'])
n=data.head()
print(n)
positive = data[data['Admitted'].isin([1])]
negative = data[data['Admitted'].isin([0])]
plt.scatter(positive['Exam 1'], positive['Exam 2'],c='r',marker='o',label='Admitted')
plt.scatter(negative['Exam 1'], negative['Exam 2'],marker='*',c='b',label='Not admitted')
plt.legend()
plt.xlabel('exam1')
plt.ylabel('exam2')
plt.show()

def sigmoid(z):
    return 1/(1+np.exp(-z))
z=np.arange(-100,100,1)
plt.plot(z,sigmoid(z),c='y',marker='*',label='验证')
plt.legend()
plt.show()
data.insert(0,'ones',1)
cols=data.shape[1]
x=data.iloc[:,:cols-1]
y=data.iloc[:,cols-1:]
x=x.values
y=y.values
theta=np.zeros((3,1))
print(theta.shape)
print(x.shape)
print(y.shape)
def  cost(x,y,theta):
    a=sigmoid(x@theta)
    first=y*np.log(a)
    second=(1-y)*(np.log(1-a))
    return -np.sum(first+second)/len(x)
print('cost',cost(x,y,theta))

def gradientDescent(x,y,theta,iters,alpha):

    for i in range(iters):
        a = sigmoid(x@theta)
        theta=theta-(alpha/len(x))*x.T@(a-y)
    return theta,cost(x,y,theta)

iters=200000
alpha=0.004
theta,cost=gradientDescent(x,y,theta,iters,alpha)
print(theta)
print('theta0',theta[0])
print('theta1',theta[1])
print('theta2',theta[2])
coef1=-(theta[0]/theta[2])
coef2=-(theta[1]/theta[2])
x=np.linspace(20,100,100)
f=coef1+coef2*x
plt.scatter(positive['Exam 1'], positive['Exam 2'],c='r',marker='o',label='Admitted')
plt.scatter(negative['Exam 1'], negative['Exam 2'],marker='*',c='b',label='Not admitted')
plt.plot(x,f,c='g',label="边界")
plt.legend()
plt.title('线性可分')
plt.xlabel('exam1')
plt.ylabel('exam2')
plt.show()