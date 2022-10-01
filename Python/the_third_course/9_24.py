#coding=gbk
import pandas
import numpy as np
import matplotlib.pyplot as plt
'''导入pandas、numpy、pyplot库'''

learning_rate=0.0001
iteration=20
m_train=3000
'''设置learning_rate、iteration、m_train初值'''

df = pandas.read_csv(r'E:\Study\Python\the_third_course\temperature_dataset.csv')
data=np.array(df)
m_all=np.shape(data)[0]#np.shape返回的是元组
m_test=m_all-m_train
d=np.shape(data)[1]-1
'''获取训练集和测试集个数和每次训练样本的个数'''

x_train=data[0:m_train,1:].T#X需要转置，按照线代思想x1~xn构成一列
x_test=data[m_train:,1:].T
y_train=data[:m_train,0].T
y_test=data[m_train:,0].T
'''将数据集划分为训练集和测试集'''


w = np.zeros((d, 1)).reshape((-1, 1))
b=0
v=np.ones((1,m_train))
costs_saved=[]
'''初始化w，b，设置v和coast_saved[]'''

for i in range(iteration):
    y_hat=np.dot(w.T,x_train)+b*v
    e=y_hat-y_train
    w=w-learning_rate*2*np.dot(x_train,e.T)/m_train
    b=b-2*learning_rate*np.dot(v,e.T)/m_train
    cost=np.dot(e,e.T)/m_train
    costs_saved.append(cost.item(0))
'''迭代训练'''

e_test=(np.dot(w.T,x_test)-y_test).reshape(-1)

plt.plot(range(1,m_test+1), e_test ,'ro--')
plt.plot(range(1,iteration+1),costs_saved,'yo--')
'''plt.ylabel('Costs')
plt.xlabel('Iterations')
plt.title('Learning rate = ' + str(learning_rate))'''
plt.show()
