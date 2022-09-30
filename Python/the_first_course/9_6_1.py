import time
sum=0
c=time.perf_counter()
count=0
a=list(range (0,1000))
b=list(range (1000,2000))
for i in range(0,1000):
    sum=sum+a[i]*b[i]
print(sum)
print(time.perf_counter()-c)
