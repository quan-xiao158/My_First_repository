#coding=gbk
import pandas
import numpy as np
import matplotlib.pyplot as plt
'''����pandas��numpy��pyplot��'''

learning_rate=0.0001
iteration=20
m_train=3000
'''����learning_rate��iteration��m_train��ֵ'''

df = pandas.read_csv(r'E:\Study\Python\the_third_course\temperature_dataset.csv')
data=np.array(df)
m_all=np.shape(data)[0]#np.shape���ص���Ԫ��
m_test=m_all-m_train
d=np.shape(data)[1]-1
'''��ȡѵ�����Ͳ��Լ�������ÿ��ѵ�������ĸ���'''

x_train=data[0:m_train,1:].T#X��Ҫת�ã������ߴ�˼��x1~xn����һ��
x_test=data[m_train:,1:].T
y_train=data[:m_train,0].T
y_test=data[m_train:,0].T
'''�����ݼ�����Ϊѵ�����Ͳ��Լ�'''


w = np.zeros((d, 1)).reshape((-1, 1))
b=0
v=np.ones((1,m_train))
costs_saved=[]
'''��ʼ��w��b������v��coast_saved[]'''

for i in range(iteration):
    y_hat=np.dot(w.T,x_train)+b*v
    e=y_hat-y_train
    w=w-learning_rate*2*np.dot(x_train,e.T)/m_train
    b=b-2*learning_rate*np.dot(v,e.T)/m_train
    cost=np.dot(e,e.T)/m_train
    costs_saved.append(cost.item(0))
'''����ѵ��'''

e_test=(np.dot(w.T,x_test)-y_test).reshape(-1)

plt.plot(range(1,m_test+1), e_test ,'ro--')
plt.plot(range(1,iteration+1),costs_saved,'yo--')
'''plt.ylabel('Costs')
plt.xlabel('Iterations')
plt.title('Learning rate = ' + str(learning_rate))'''
plt.show()
