import matplotlib.pyplot as plt
import numpy as np
plt.figure()
x=np.linspace(-1,6,10)
y=(2*x-3)**2+4

plt.plot(x,y)
plt.show()