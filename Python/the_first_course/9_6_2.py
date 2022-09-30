import numpy as np
import time
t=time.perf_counter()
a=np.arange(0,1000)
b=np.arange(1000,2000)
print(np.dot(a,b))
print(time.perf_counter()-t)