import pandas
import numpy as np
import matplotlib.pyplot as plt

df=pandas.read_csv(r'E:\Study\Python\the_third_course\temperature_dataset.csv')
data=np.array(df)

learning_rate=0.0001
m_train=3000
iteration=20
m_all=data.shape[0]
d=data.shape[1]-1
x_train=data[:m_train,1:].T
x_test=data[m_train:,1:].T
y_train=data[0:m_train,0].T
y_test=data[m_train:,0].T
w=np.zeros((d,1)).reshape(4,1)
b=0


v=np.ones((m_train,1)).reshape(m_train,1)
cost_saved=[]

for i in range(iteration):
    y_hat=np.dot(w.T,x_train)+b
    e=y_hat-y_train
    w=w-2*learning_rate*np.dot(x_train,e.T)/m_train
    b=b-2*learning_rate*np.dot(e,v)/m_train
    cost=np.dot(e,e.T).item(0)/m_train
    cost_saved.append(cost)

y_hat_train=np.dot(w.T,x_train)+b*v.T
e=y_hat_train-y_train


y_hat_train=np.dot(w.T,x_test)+b
e=y_hat_train-y_test
print(np.sqrt(np.dot(e,e.T).item(0)/m_train))
plt.plot(range(1,iteration+1),cost_saved)
plt.show()

