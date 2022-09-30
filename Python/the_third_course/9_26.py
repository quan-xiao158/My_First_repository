#coding=gbk
from tkinter import E
import numpy as np
import pandas
import matplotlib.pyplot as plt 

learning_rate=0.0001
train_number=3000
iteration=20


df=pandas.read_csv(r'E:\Study\Python\the_third_course\temperature_dataset.csv')
data=np.array(df)
d=data.shape[1]-1 #训练中x输入的个数
x_train=data[:train_number,1:].T
y_train=data[:train_number,0].reshape(1,-1)
x_test=data[train_number:,1:].T
y_test=data[train_number:,0].reshape(1,-1)
w=np.zeros((1,d)).reshape(-1,1)
b=0
v=np.ones((1,train_number)).reshape(train_number,1)
cost_saved=[]
cost=0





for i in range(0,iteration):
    y_hat=np.dot(w.T,x_train)+b
    e=y_hat-y_train
    w=w-learning_rate*np.dot(x_train,e.T)*2/train_number
    b=b-learning_rate*np.dot(e,v)*2/train_number
    cost=np.dot(e,e.T)
    cost_saved.append(cost.item(0))


plt.plot(range(1,iteration+1),cost_saved)
plt.show()





