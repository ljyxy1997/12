import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
path = 'data/regress_data1.csv'
data = pd.read_csv(path)
data.head() #默认读取前5行数据
print(data.head())
data.describe() #计算出数组的个数、平均值、标准差、最小值、25、50、75，最大值
data.plot(kind='scatter', x='人口', y='收益', figsize=(12,8))#kind:图的种类，figsize(a,b):a为X轴长，b为Y轴长
plt.xlabel('人口',fontsize=18) #frontsize:人口字体大小
plt.ylabel('收益', rotation=0, fontsize=18) #rotation:收益字体的旋转角度
plt.show()

def computeCost(X, y, w):
    inner = np.power(((X * w.T) - y), 2)# (m,n) @ (n, 1) -> (n, 1)
#     return np.sum(inner) / (2 * len(X))
    return np.sum(inner) / (2 * X.shape[0]) #shape[0]是第一维（列）长度，shape(1)是第二维[行]长度
data.insert(0, 'Ones', 1)
# set X (training data) and y (target variable)
cols = data.shape[1]
X = data.iloc[:,:cols-1]#X是所有行，去掉最后一列，取到cols-1列。 .iloc[a:b,c:d]取（a+1到b行，c+1到d列）的数据
y = data.iloc[:,cols-1:]#y是最后一列
X = np.matrix(X.values)  #values用来将字典中所有的值读出来 matrix将读取的值转成矩阵
y = np.matrix(y.values)
w = np.matrix(np.array([0,0]))
computeCost(X, y, w)
print(computeCost(X, y, w))

def batch_gradientDescent(X, y, w, alpha, iters):   #定义批量梯度下降函数
    temp = np.matrix(np.zeros(w.shape))  #为了存放w, np.zeros(a,b) 生成一个a行b列的零矩阵，w.shape：读出w这个矩阵的形状。即生成一个和w同形状的零矩阵
    parameters = int(w.ravel().shape[1]) #为了计算出w的个数 w.ravel()将矩阵变成一行
    cost = np.zeros(iters)  #为了存放代价函数 iters:迭代次数

    for i in range(iters):
        error = (X * w.T) - y

        for j in range(parameters):
            term = np.multiply(error, X[:, j])
            temp[0, j] = w[0, j] - ((alpha / len(X)) * np.sum(term)) #w[0, j]代表矩阵第一行，第j+1位置的元素

        w = temp
        cost[i] = computeCost(X, y, w)

    return w, cost
alpha = 0.01
iters = 1000
g,cost= batch_gradientDescent(X, y, w, alpha, iters)
print(g)
print(computeCost(X, y, g))

x = np.linspace(data['人口'].min(), data['人口'].max(), 100) #np.linspace(a,b,c) 从a到b以等差数列的方式生成c个数
f = g[0, 0] + (g[0, 1] * x)

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x, f, 'r', label='预测值')  #scatter绘制散点，plot绘制经过点的曲线。
ax.scatter(data['人口'], data['收益'], label='训练数据')
ax.legend(loc=2) #设置图例位置
ax.set_xlabel('人口', fontsize=18)
ax.set_ylabel('收益', rotation=0, fontsize=18)
ax.set_title('预测收益和人口规模', fontsize=18)
plt.show()

fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(np.arange(iters), cost, 'r')
ax.set_xlabel('迭代次数', fontsize=18)
ax.set_ylabel('代价', rotation=0, fontsize=18)
ax.set_title('误差和训练Epoch数', fontsize=18)
plt.show()

path = 'data/regress_data2.csv'
data2 = pd.read_csv(path)
data2.head()
data2 = (data2 - data2.mean()) / data2.std()
data2.head()
# add ones column
data2.insert(0, 'Ones', 1)

# set X (training data) and y (target variable)
cols = data2.shape[1]
X2 = data2.iloc[:,0:cols-1]
y2 = data2.iloc[:,cols-1:cols]

# convert to matrices and initialize theta
X2 = np.matrix(X2.values)
y2 = np.matrix(y2.values)
w2 = np.matrix(np.array([0,0,0]))
# perform linear regression on the data set
g2, cost2 = batch_gradientDescent(X2, y2, w2, alpha, iters)

# get the cost (error) of the model
computeCost(X2, y2, g2)
print(computeCost(X2, y2, g2))

fig, ax = plt.subplots(figsize=(12,8))
ax.plot(np.arange(iters), cost2, 'r')
ax.set_xlabel('迭代次数', fontsize=18)
ax.set_ylabel('代价', rotation=0, fontsize=18)
ax.set_title('误差和训练Epoch数', fontsize=18)
plt.show()

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X, y) #对训练集X y进行训练
x = np.array(X[:, 1].A1)
f = model.predict(X).flatten() #使用 predict(x_test) 训练得到的估计器对输入为 x_test 的集合进行预测
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x, f, 'r', label='预测值')
ax.scatter(data['人口'], data['收益'], label='训练数据')
ax.legend(loc=2, fontsize=18)
ax.set_xlabel('人口', fontsize=18)
ax.set_ylabel('收益', rotation=0, fontsize=18)
ax.set_title('预测收益和人口规模', fontsize=18)
plt.show()

from sklearn.linear_model import Ridge
model = Ridge()
model.fit(X, y)
x2 = np.array(X[:, 1].A1)
f2 = model.predict(X).flatten()
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x2, f2, 'r', label='预测值Ridge')
ax.scatter(data['人口'], data['收益'], label='训练数据')
ax.legend(loc=2, fontsize=18)
ax.set_xlabel('人口', fontsize=18)
ax.set_ylabel('收益', rotation=0, fontsize=18)
ax.set_title('预测收益和人口规模', fontsize=18)
plt.show()

from sklearn.linear_model import Lasso
model = Lasso()
model.fit(X, y)
x3= np.array(X[:, 1].A1)
f3 = model.predict(X).flatten()
fig, ax = plt.subplots(figsize=(12, 8))
ax.plot(x3, f3, 'r', label='预测值Lasso')
ax.scatter(data['人口'], data['收益'], label='训练数据')
ax.legend(loc=2, fontsize=18)
ax.set_xlabel('人口', fontsize=18)
ax.set_ylabel('收益', rotation=0, fontsize=18)
ax.set_title('预测收益和人口规模', fontsize=18)
plt.show()

from sklearn.model_selection import cross_val_score #交叉验证
alphas = np.logspace(-3, 2, 50)
test_scores = []
for alpha in alphas:
    clf = Ridge(alpha)
    test_score = np.sqrt(-cross_val_score(clf, X, y, cv=5, scoring='neg_mean_squared_error'))
    test_scores.append(np.mean(test_score))
import matplotlib.pyplot as plt
plt.plot(alphas, test_scores)
plt.title("Alpha vs CV Error");
plt.show()

def LSM(X, y):
    w = np.linalg.inv(X.T@X)@X.T@y#X.T@X等价于X.T.dot(X)
    return w
final_w2=LSM(X, y)#感觉和批量梯度下降的theta的值有点差距
final_w2