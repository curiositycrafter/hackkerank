import numpy as n
k=[]
l=list(map(int,input().split()))
for i in range(l[0]):
    t=list(map(int, input().split()))
    k.append(t)
v=n.sum(k,axis=0)
print(n.prod(v))
