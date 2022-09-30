import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-5,5,1000)
y1=abs(2*x-1)
y2=abs(2*x+1)
y3=0.5*y1+0.3*y2
plt.figure()
plt.plot(y1)
plt.plot(y2)
plt.plot(y3)
plt.show()