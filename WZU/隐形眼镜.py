import numpy as np
import pandas as pd
from sklearn import tree
from sklearn.preprocessing import LabelEncoder #标准化标签，将标签值统一转换成range(标签值个数-1)范围内
from sklearn.model_selection import train_test_split
import graphviz
path='data/lenses.txt'
dataset=pd.read_csv(path,sep='\t',names=['age','prescript','astigmatic','tearrate','class'])
l = LabelEncoder()
feature_name=['age','prescript','astigmatic','tearrate']
#创建LabelEncoder对象，用于序列化
for col in dataset.columns: #把字符转成数字
    dataset[col] = l.fit_transform(dataset[col])
    #以每一列的特征为标准进行序列化
    #fit_transform的作用就是先拟合数据，然后转化它为标准形式
print(dataset.shape)
#print(dataset.iloc[:,:-1])
Xtrain,Xtest,Ytrain,Ytest=train_test_split(dataset.iloc[:,:-1]
                                           ,dataset.iloc[:,-1]
                                           ,test_size=0.3)
clf=tree.DecisionTreeClassifier(criterion='entropy')
clf=clf.fit(Xtrain,Ytrain)
score=clf.score(Xtest,Ytest)
#print(score)
import graphviz
dot_data = tree.export_graphviz(clf
                                ,feature_names=feature_name
                                ,class_names=['soft','hard','no lense']
                                ,filled=True
                                ,rounded=True)
graph=graphviz.Source(dot_data)
graph.view() #显示决策树